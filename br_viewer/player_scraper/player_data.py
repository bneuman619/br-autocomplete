from db_setup import Session, Player, StatTable, TableType, Year
from scrape_player import scrape_player_to_db
from stat_columns import stat_columns
import pandas as pd


SESSION = Session()

def get_player_data(player_name):
    rows = get_player_rows(player_name)
    data = PlayerData(player_name, rows)
    return data

def get_player_rows(player_name):
    player = SESSION.query(Player).filter(Player.name.like(player_name)).first()
    rows = lookup_player_stat_rows(player)
      
    if not rows:
        scrape_player_to_db(player_name)
        rows = lookup_player_stat_rows(player)
      
    return rows

def lookup_player_stat_rows(player):
    rows = SESSION.query(StatTable).filter(StatTable.player_id==player.id).all()
    return rows


class PlayerData:
    def __init__(self, player_name, rows):
        self.name = player_name
        self.rows = rows
        self.columns = stat_columns

    def __getitem__(self, key):
        items = []

        for row in self.rows:
            if (row.type.type_name.lower() == key.lower()) or (row.year.year == key):
                items.append(row)

        return items

    def get_totals(self, stat):
        return self._get_stat_of_type(stat, 'totals')

    def get_per_game(self, stat):
        return self._get_stat_of_type(stat, 'per_game')

    def get_per_minute(self, stat):
        return self._get_stat_of_type(stat, 'per_minute')
      
    def _get_stat_of_type(self, stat, stat_type):
        if stat not in self.columns:
            return None

        stats = {}

        for row in self.rows:
            if (row.type.type_name.lower() == stat_type):
                stats[row.year.year] = row.__dict__[stat]

        stats_series = pd.Series(stats)
        return stats_series        

