import pandas as pd
import numpy as np

class StatsTable:
    def __init__(self, stat_dicts, id):
        self.stat_dicts = stat_dicts
        self.name = id
        self.panda, self.career_panda = self.build_data_frames()

    def __getitem__(self, key):
        if key.lower() == 'career':
            return self.career_stats()

        try:
            item = self.panda[key]

        except KeyError:
            try:
                item = self.panda.loc[key]

            except KeyError:
                raise KeyError

            else:
                return item

        else:
            return item

    def __repr__(self):
        return self.complete_table().__repr__()

    def indices(self):
        return self.panda.index.values

    def view_stats(self):
        return self.stats().transpose()

    def stats(self):
        return self.panda

    def view_career_stats(self):
        return self.career_stats().transpose()

    def career_stats(self):
        return self.career_panda

    def view_complete_table(self):
        return self.complete_table().transpose()

    def complete_table(self):
        return self.panda.join(self.career_panda)

    def build_data_frames(self):
        series_dict = {}
        for stat_dict in self.stat_dicts:
            year = stat_dict.pop('Season')
            panda = pd.Series(data=stat_dict)
            series_dict[year] = panda

        career = {'Career': series_dict.pop("Career") }

        data_frame = pd.DataFrame(series_dict)
        career_frame = pd.DataFrame(career)

        return data_frame, career_frame