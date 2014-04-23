from db.setup import *

class Year(Base):
    __tablename__ = "years"
    id = Column(Integer, Sequence('table_types_id_seq'), primary_key=True)
    year = Column(String)