from br_player_finder import get_player_soup
from db_setup import Session, Player, StatTable, TableType, Year
from stat_columns import stat_columns
import re

def scrape_player_to_db(player_name):
    soup = get_player_soup(player_name)
    tables = get_parsed_tables(soup)

    session = Session()
    player_id = session.query(Player).filter(Player.name.like(player_name)).first().id


    ready_rows = []

    for table in tables:
        type_id = session.query(TableType).filter(TableType.type_name==table['table_name']).first().id

        for row in table['rows']:
            row['year_id'] = session.query(Year).filter(Year.year==row['year']).first().id
            row['type_id'] = type_id
            row['player_id'] = player_id
            row.pop('year')
            session.add(StatTable(**row))

    try:
        session.commit()

    except:
        raise

    else:
        return player_id


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

