import requests
import re
from bs4 import BeautifulSoup as BS
''' [
        {'movie_name':
             {'rating': INT,
             'cinemas_count': INT'
             }
        },
    ...]
'''
def fetch_afisha_page():
    page = requests.get('http://www.afisha.ru/msk/schedule_cinema/').text
    return page
    

def parse_afisha_list(raw_html):
    bs = BS(raw_html, 'html.parser')
    movies_list = bs.find(id='schedule').find_all(class_='m-disp-table')
    movies_info = dict()
    for movie in movies_list:
        cinemas = movie.next_sibling.next_sibling.find_all(class_='b-td-item')
        movies_info[movie.h3.string] = {'cinemas' : len(cinemas)}

    
def fetch_movie_info(movie_title):
    pass


def output_movies_to_console(movies):
    pass


if __name__ == '__main__':
    afisha_page = fetch_afisha_page()
    parsed_afisha = parse_afisha_list(afisha_page)
