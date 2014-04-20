import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref
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

class TableType(Base):
    __tablename__ = 'table_types'
    id = Column(Integer, Sequence('table_types_id_seq'), primary_key=True)
    type_name = Column(String)

class Year(Base):
    __tablename__ = "years"
    id = Column(Integer, Sequence('table_types_id_seq'), primary_key=True)
    year = Column(String)


class RegularStat(Base):
    __tablename__ = 'stats'

    id = Column(Integer, Sequence('regular_stats_id_seq'), primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    year_id = Column(Integer, ForeignKey('years.id'))
    type_id = Column(Integer, ForeignKey('table_types.id'))
    games = Column(Integer)
    games_started = Column(Integer)
    minutes_played = Column(Integer)
    fgs = Column(Integer)
    fg_attempts = Column(Integer)
    fg_percent = Column(Float)
    th_fgs = Column(Integer)
    th_fg_attempts = Column(Integer)
    th_fg_percent = Column(Float)
    tw_fgs = Column(Integer)
    tw_fg_attempts = Column(Integer)
    tw_fg_percent = Column(Float)
    fts = Column(Integer)
    ft_attempts = Column(Integer)
    ft_percent = Column(Float)
    off_rebound = Column(Integer)
    def_rebound = Column(Integer)
    rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    fouls = Column(Integer)
    points = Column(Integer)

    player = relationship("Player", backref=backref('stat_tables', order_by=id))
    year = relationship("Year")
    type = relationship("TableType")


Base.metadata.create_all(engine)