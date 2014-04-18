from soupify import soupify
from br_player_scraper import make_player_stats

def get_curry_soup():
    return soupify('http://www.basketball-reference.com/players/c/curryst01.html')

def make_curry():
    curry = get_curry_soup()
    stats = make_player_stats(curry)
    return stats