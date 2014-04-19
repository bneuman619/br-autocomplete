import sqlalchemy
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('sqlite:///player_db.db', echo=True)
Base = declarative_base()
Session = sqlalchemy.orm.sessionmaker(bind=engine)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    name = Column(String)
    url = Column(String)

    def __repr__(self):
        return "<Name: %s, url: %s>" % (self.name, self.url)

    
Base.metadata.create_all(engine)