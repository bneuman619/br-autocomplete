from soupify import soupify
from db import Player, Session

session = Session()

def get_player_soup(player_name):
    url = get_player_url(player_name)
    soup = soupify(url)
    return soup

def get_player_url(player_name):
    url = get_player_url_from_db(player_name)

    if not url:
        url = get_player_url_from_br(player_name)
    
        if not url:
            return None

    absolute_url = "http://basketball-reference.com" + url
    return absolute_url

def get_player_url_from_db(player_name):
    player = session.query(Player).filter(Player.name.like(player_name.lower())).first()
    if player:
        return player.url
    else:
        return None

def get_player_url_from_br(player_name):
    index_url = get_index_url_from_name(player_name)
    souped_index = soupify(index_url)
    link_finder = player_link_finder(player_name)
    player_link_element = souped_index.find(link_finder)
    if player_link_element:
        link = player_link_element['href']
        return link
    else:
        return None

def player_link_finder(name):
    def link_finder(element):
        return (element.name == 'a') and (element.text.lower() == name.lower())
   
    return link_finder

def get_first_letter_of_last_name(player_name):
    last_name = player_name.split(" ")[-1]
    return last_name[0].lower()

def get_index_url_from_name(player_name):
    letter = get_first_letter_of_last_name(player_name)
    return "http://basketball-reference.com/players/" + letter
