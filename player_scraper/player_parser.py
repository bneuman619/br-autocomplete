import re
from stat_columns import stat_columns

def get_parsed_tables(stats_doc):
    tables = get_tables(stats_doc)
    parsed_tables = [parse_table(table) for table in tables]
    return parsed_tables

def get_tables(stats_doc):
    table_ids = ['totals', 'per_game', 'per_minute']
    tables = stats_doc.find_all('table', id=table_ids)
    return tables

def parse_table(table):
    rows = get_rows(table)
    parsed_rows = parse_rows(rows)
    parsed_table = {'table_name': table['id'], 'rows': parsed_rows}
    return parsed_table

def get_rows(table):
    year_rows = table.find_all(name='tr', class_='full_table')
    return year_rows

def parse_rows(rows):
    parsed_rows = [get_parsed_row_contents(row) for row in rows]
    return parsed_rows

def get_parsed_row_contents(row):
    contents = get_row_contents(row)
    row_dict = dict(zip(stat_columns, contents[5:]))
    row_dict['year'] = contents[0]
    return row_dict

def get_row_contents(row):
    cells = row.find_all('td')
    row_contents = [get_cell_contents(cell) for cell in cells]
    return row_contents

def get_cell_contents(cell):
    cell_contents = cell.text.encode('ascii', 'ignore')

    if re.match('\.\d+$', cell_contents):
        cell_contents = int(float(cell_contents) * 100)

    return cell_contents

