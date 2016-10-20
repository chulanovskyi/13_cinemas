import requests
import re
from argparse import ArgumentParser
from bs4 import BeautifulSoup as BS


AFISHA_URL = 'http://www.afisha.ru/msk/schedule_cinema/'
KINOPOISK_URL = 'https://www.kinopoisk.ru/index.php'
NO_BREAK_SPACE = '\xa0'


def fetch_afisha_page():
    page = requests.get(AFISHA_URL).text
    return page
    

def parse_afisha_list(raw_html):
    bs = BS(raw_html, 'html.parser')
    movies_list = bs.find(id='schedule').find_all(class_='m-disp-table')
    movies_titles_and_meta = dict()
    for movie in movies_list:
        movie_title = movie.h3.string
        cinemas = movie.next_sibling.next_sibling.find_all(class_='b-td-item')
        movies_titles_and_meta[movie_title] = {'cinemas' : len(cinemas)}
    return movies_titles_and_meta


def fetch_movie_info(title, info):
    movie = {title: info}
    movie[title].update({'rating': 0, 'votes': 0})
    query_params = {'kp_query': title}
    search_query = requests.get(KINOPOISK_URL, params=query_params).text
    bs = BS(search_query, 'html.parser')
    kp_info = bs.find(class_='element most_wanted')
    if not kp_info:
        return movie
    rating_block = kp_info.find(class_='rating')
    if not rating_block:
        return movie
    cut_items = [NO_BREAK_SPACE,'(',')']
    try:
        rating, votes = replace_all(rating_block['title'], cut_items, '').split()
    except ValueError:
        rating = rating_block.string
        votes = replace_all(rating_block['title'], cut_items, '')
    movie[title].update({'rating': float(rating), 'votes': int(votes)})
    return movie


def input_sort_attr():
    SORT_RATING, SORT_CINEMAS = (1,2)
    sort_by = input('Sort movies by:\n' +
                    '{by_rating}. Rating\n{by_cinemas}. Cinemas\n'.format(
                        by_rating=SORT_RATING,
                        by_cinemas=SORT_CINEMAS))
    if sort_by == '1':
        return 'rating'
    elif sort_by == '2':
        return 'cinemas'
    else:
        raise ValueError('Wrong input: {choice}\nAllowed inputs: 1, 2'.format(
            choice=sort_by))


def sort_movies(movies, attr):
    sort_by_attr = sorted(movies.items(),
                          key=lambda title_info: title_info[1][attr],
                          reverse=True)
    return sort_by_attr


def output_movies_to_console(movies, attr):
    for ind, movie in enumerate(movies, 1):
        title, info = movie
        print(str(ind)+'. {title} ({attr})'.format(
            title=title,
            attr=info[attr]))


def replace_all(text, cut_items, new_item):
    for item in cut_items:
        text = text.replace(item, new_item)
    return text


def create_parser():
    parser = ArgumentParser()
    parser.add_argument(
        '--movies',
        type=int,
        default=10,
        help='Output movies list size')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    output_list_size = parser.parse_args().movies
    afisha_page = fetch_afisha_page()
    try:
        sort_attr = input_sort_attr()
    except ValueError as err:
        print(err)
        exit(11)
    print('Parsing and sorting...')
    parsed_afisha = parse_afisha_list(afisha_page)
    for title, info in parsed_afisha.items():
        parsed_afisha.update(fetch_movie_info(title, info))
    sorted_afisha = sort_movies(parsed_afisha, sort_attr)[:output_list_size]
    output_movies_to_console(sorted_afisha, sort_attr)
