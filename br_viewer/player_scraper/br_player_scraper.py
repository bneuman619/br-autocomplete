from table_ids import table_ids
from player_stats import PlayerStats
from stats_table import StatsTable
import pandas as pd
import numpy as np

def find_header_row(table):
    rows = table.find_all('tr')
    for row in rows:
        if row['class'] == ['']:
            return row.find_all('th')

def find_stat_rows(table):
    rows = []
    for row in table.find_all(name='tr', class_='full_table'):
        row_cells = row.find_all('td')
        rows.append(row_cells)

    return rows

def find_career_stat_row(table):
    return table.find(class_='stat_total').find_all('td')

def get_row_contents(row, strip_percent=False):
    row_contents = []
    for cell in row:
        cell_contents = cell.text.encode('ascii', 'ignore')
        if strip_percent:
            cell_contents = cell_contents.strip("%")
        row_contents.append(cell_contents)

    return row_contents

def get_headers(table):
    row = find_header_row(table)
    contents = get_row_contents(row)
    return contents

def get_stat_rows(table):
    stat_rows = find_stat_rows(table)
    rows = []
    for stat_row in stat_rows:
        contents = get_row_contents(stat_row, strip_percent=True)
        rows.append(contents)
    return rows

def get_rows_as_dicts(table):
    stat_rows = get_stat_rows(table)
    headers = get_headers(table)
    dict_rows = []
    for stat_row in stat_rows:
        dict_row = get_stat_dict(headers, stat_row)
        dict_rows.append(dict_row)
    return dict_rows

def get_stat_dict(headers, row):
    stat_dict = dict(zip(headers, row))
    return stat_dict

def get_career_stat_row(table):
    row = find_career_stat_row(table)
    contents = get_row_contents(row)
    return contents

def get_years(rows):
    years = []
    for row in rows:
        year = rows[0]
        years.append(year)
    return years

def process_table(table):
    stat_dicts = get_rows_as_dicts(table)
    id = table['id']
    data_frame = build_data_frame_for_table(stat_dicts)
    return id, data_frame

def get_tables(stats_doc):
    tables = stats_doc.find_all('table', id=table_ids)
    return tables

def get_player_name(doc):
    return doc.h1.text

def make_player_stats(soup_doc):
    tables = get_tables(soup_doc)
    processed_tables = {}

    for table in tables:
        id, data_frame = process_table(table)
        processed_tables[id] = data_frame

    name = get_player_name(soup_doc)
    stats = PlayerStats(name, processed_tables)
    return stats

def build_data_frame_for_table(stat_dicts):
    series_dict = {}
    for stat_dict in stat_dicts:
        year = stat_dict.pop('Season')
        stat_dict.pop("Lg")
        stat_dict.pop("Tm")
        stat_dict.pop("Pos")
        floated = float_stat_dict(stat_dict)
        panda = pd.Series(data=floated)
        series_dict[year] = panda

    data_frame = pd.DataFrame(series_dict)

    return data_frame

def float_stat_dict(stat_dict):
    floated_dict = {}
    for key in stat_dict:
        try:
            floated_dict[key] = float(stat_dict[key])

        except ValueError:
            floated_dict[key] = 0

    return floated_dict