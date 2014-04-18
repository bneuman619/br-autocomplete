import httplib2
from bs4 import BeautifulSoup

def soupify(url):
    h = httplib2.Http()
    resp, content = h.request(url)
    soup = BeautifulSoup(content)
    return soup
