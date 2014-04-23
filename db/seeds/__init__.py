from players import seed_players
from table_types import seed_table_types
from years import seed_years
from db.setup import *

def seed():
    seed_players()
    seed_table_types()
    seed_years()
