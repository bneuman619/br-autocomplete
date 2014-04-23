from player_fetcher import get_player_soup
from player_parser import get_parsed_tables
from db import Session, Player, StatTable, TableType, Year
from stat_columns import stat_columns

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
