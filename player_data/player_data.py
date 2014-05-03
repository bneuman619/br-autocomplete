import pandas as pd
from player_scraper import stat_columns

class StatTypeError(Exception):
    pass

class PlayerData:
    def __init__(self, player_name, rows):
        self.name = player_name
        self.rows = rows
        self.columns = rows[0].keys()

    def __getitem__(self, key):
        items = []

        for row in self.rows:
            if (row.type.type_name.lower() == key.lower()) or (row.year.year == key):
                items.append(row)

        return items

    def get_stat_types(self):
        return self.columns

    def get_table_types(self):
        return ['totals', 'per_game', 'per_minute']

    def graph(self, stat_type, table_type):
        if stat_type not in self.columns:
            raise StatTypeError

        if table_type == 'totals':
            self.graph_totals(stat_type)

        elif table_type == 'per_game':
            self.graph_per_game(stat_type)

        elif table_type == 'per_minute':
            self.graph_per_minute(stat_type)

        else:
            raise StatTypeError

    def graph_totals(self, stat_type):
        self.get_totals(stat_type).plot()

    def graph_per_game(self, stat_type):
        self.get_per_game(stat_type).plot()

    def graph_per_minute(self, stat_type):
        self.get_per_minute(stat_type).plot()
          
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
            if (row['type'].lower() == stat_type):
                stats[row['year']] = row[stat]

        stats_series = pd.Series(stats)
        return stats_series        

