import pandas as pd
import numpy as np


def build_data_frame_for_table(table):
    series_dict = {}
    for stat_dict in table:
        year = stat_dict.pop('Season')
        stat_dict.pop("Lg")
        stat_dict.pop("Tm")
        panda = pd.Series(data=stat_dict, dtype='float')
        series_dict[year] = panda

    data_frame = pd.DataFrame(series_dict)

    return data_frame