from db.setup import *
from db.models import *

def seed_years():
    session = Session()
    session.add(Year(year='Career'))

    year_range = range(1946, 2014)
    for year in year_range:
        year_string = str(year) + "-" + str(year + 1)[-2:]
        session.add(Year(year=year_string))

    session.commit()