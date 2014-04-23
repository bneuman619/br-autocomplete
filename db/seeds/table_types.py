from db.setup import *
from db.models import *

def seed_table_types():
    session = Session()
    session.add(TableType(type_name='totals'))
    session.add(TableType(type_name='per_game'))
    session.add(TableType(type_name='per_minute'))
    session.commit()