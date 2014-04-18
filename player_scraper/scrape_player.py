from br_player_finder import get_player_soup
from br_player_scraper import make_player_stats

def scrape_player(player_name):
    soup = get_player_soup(player_name)
    stats = make_player_stats(stats)
    return stats