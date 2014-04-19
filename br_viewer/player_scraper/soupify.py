import httplib2
from bs4 import BeautifulSoup

def soupify(url):
    content = get_url_content(url)
    soup = BeautifulSoup(content)
    return soup

def get_url_content(url):
    h = httplib2.Http()
    resp, content = h.request(url)
    return content