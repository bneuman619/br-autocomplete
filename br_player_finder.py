from bs4 import BeautifulSoup as bs
import httplib2

def soupify(url):
    content = get_url_content(url)
    soup = bs(content)
    return soup

def get_url_content(url):
    h = httplib2.Http()
    resp, content = h.request(url)
    return content


def get_first_letter_of_last_name(player_name):
    last_name = player_name.split(" ")[-1]
    return last_name[0].lower()

def get_index_url_from_name(player_name):
    letter = get_first_letter_of_last_name(player_name)
    return "http://basketball-reference.com/players/" + letter

def get_player_url(player_name):
    index_url = get_index_url_from_name(player_name)
    souped_index = soupify(index_url)
    link_finder = player_link_finder(player_name)
    player_link = souped_index.find(link_finder)
    relative_link = player_link['href']
    absolute_url = "http://basketball-reference.com" + relative_link
    return absolute_url

def get_player_page(player_name):
    url = get_player_url(player_name)
    content = get_url_content(url)
    return content

def player_link_finder(name):
    if name[0] == " ":
        name = name[1:]

    def link_finder(element):
        return (element.name == 'a') and (element.text.lower() == name.lower())
   
    return link_finder
