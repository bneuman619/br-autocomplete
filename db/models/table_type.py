from db.setup import *

class TableType(Base):
    __tablename__ = 'table_types'
    id = Column(Integer, Sequence('table_types_id_seq'), primary_key=True)
    type_name = Column(String)
