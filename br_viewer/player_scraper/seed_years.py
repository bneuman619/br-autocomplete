import db_setup
from db_setup import Year, Session, TableType

def seed_years():
    year_range = range(1946, 2014)
    session = Session()

    for year in year_range:
        year_string = str(year) + "-" + str(year + 1)[-2:]
        session.add(Year(year=year_string))

    session.commit()

def seed_table_types():
    session = Session()
    session.add(TableType(type_name='totals'))
    session.add(TableType(type_name='per_game'))
    session.add(TableType(type_name='per_36'))
    session.commit()

seed_years()
seed_table_types()


