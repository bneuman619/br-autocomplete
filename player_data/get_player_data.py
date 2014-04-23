from player_data import PlayerData
from db import Player, StatTable, Session
from player_scraper import scrape_player_to_db

session = Session()

def get_player_data(player_name):
    rows = get_player_rows(player_name)
    data = PlayerData(player_name, rows)
    return data

def get_player_rows(player_name):
    player = session.query(Player).filter(Player.name.like(player_name)).first()
    rows = lookup_player_stat_rows(player)
      
    if not rows:
        scrape_player_to_db(player_name)
        rows = lookup_player_stat_rows(player)
      
    return rows

def lookup_player_stat_rows(player):
    rows = session.query(StatTable).filter(StatTable.player_id==player.id).all()
    return rows
