import setup
import re
import httplib2
from bs4 import BeautifulSoup
from setup import Player
from setup import Session

base_url = 'http://www.basketball-reference.com/players/'

def seed():
    session = Session()
    links = get_all_links()
    
    for link in links:
        player_object = make_player_object_from_link(link)
        session.add(player_object)
    
    session.commit()
    session.close()

def make_player_object_from_link(link):
    url = link['href']
    name = str(link.text.encode('ascii', 'ignore'))
    return Player(name=name, url=url)

def get_all_links():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',\
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    links = []
    for letter in alphabet:
        links += get_player_links_for_letter(letter)

    return links


def get_player_links_for_letter(letter):
    url = base_url + letter + '/'
    soup = soupify(url)
    finder = player_link_finder_for_letter(letter)
    links = soup.find_all(finder)
    return links

def make_regex_for_letter(letter):
    return re.compile("\/players\/%s\/.*\.html" % letter)

def player_link_finder_for_letter(letter):
    regex = make_regex_for_letter(letter)

    def link_finder(element):
        return element.name == 'a' and regex.match(element['href'])

    return link_finder

def soupify(url):
    content = get_url_content(url)
    soup = BeautifulSoup(content)
    return soup

def get_url_content(url):
    h = httplib2.Http()
    resp, content = h.request(url)
    return content

seed()
