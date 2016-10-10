import requests
import re
from bs4 import BeautifulSoup as BS
''' [
        {'movie_title':
             {'in_cinemas': INT',
              'rating': INT
             }
        },
        ...
    ]
'''
def fetch_afisha_page():
    page = requests.get('http://www.afisha.ru/msk/schedule_cinema/').text
    return page
    

def parse_afisha_list(raw_html):
    bs = BS(raw_html, 'html.parser')
    movies_list = bs.find(id='schedule').find_all(class_='m-disp-table')
    movies_info = dict()
    for movie in movies_list:
        movie_title = movie.h3.string
        cinemas = movie.next_sibling.next_sibling.find_all(class_='b-td-item')
        movies_info[movie_title] = {'in_cinemas' : len(cinemas)}
    return movies_info

    
def fetch_movie_info(movie_title):
    query_params = {'kp_query': movie_title}
    search_query = requests.get('https://www.kinopoisk.ru/index.php',
                                params=query_params).text
    bs = BS(search_query, 'html.parser')
    movie_info = bs.find(class_='element most_wanted')
    if movie_info:            
        rating = movie_info.find(class_='rating')
    if rating:
        votes = rating['title'].replace(u'\xa0',u'')
    print(type(rating['title']))
    print(votes)
        

def output_movies_to_console(movies):
    pass


if __name__ == '__main__':
    afisha_page = fetch_afisha_page()
    parsed_afisha = parse_afisha_list(afisha_page)
    test_movie = list(parsed_afisha.keys())[0] 
    print(test_movie)
    fetch_movie_info(test_movie)
