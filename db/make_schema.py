from setup import *
from models import *

def make_schema():
    Base.metadata.create_all(engine)