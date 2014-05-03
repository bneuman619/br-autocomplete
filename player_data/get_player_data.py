from player_data import PlayerData
from db import Player, StatTable, Session
from player_scraper import scrape_player_to_db

session = Session()

def get_player_data(player_name):
    rows = get_player_rows(player_name)
    row_dicts = [row_to_dict(row, player_name) for row in rows]
    data = PlayerData(player_name, row_dicts)
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


def row_to_dict(row, player_name):
    output_dict = row.__dict__
    output_dict['year'] = row.year.year
    output_dict['type'] = row.type.type_name
    output_dict['player'] = player_name
    output_dict = remove_empties(output_dict)
    return output_dict

def remove_empties(row):
    new_row = {}

    for key in row:
        if row[key]:
            new_row[key] = row[key]

    return new_row