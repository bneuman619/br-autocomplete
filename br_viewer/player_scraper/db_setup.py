import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import os

engine = sqlalchemy.create_engine('sqlite:////users/bneuman/br-suggest/br_viewer/player_scraper/player_db.db', echo=True)
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


class StatTable(Base):
    __tablename__ = 'stats'

    id = Column(Integer, Sequence('regular_stats_id_seq'), primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    year_id = Column(Integer, ForeignKey('years.id'))
    type_id = Column(Integer, ForeignKey('table_types.id'))
    games = Column(Integer)
    games_started = Column(Integer)
    minutes_played = Column(Integer)
    fgs = Column(Float)
    fg_attempts = Column(Float)
    fg_percent = Column(Float)
    th_fgs = Column(Float)
    th_fg_attempts = Column(Float)
    th_fg_percent = Column(Float)
    tw_fgs = Column(Float)
    tw_fg_attempts = Column(Float)
    tw_fg_percent = Column(Float)
    fts = Column(Float)
    ft_attempts = Column(Float)
    ft_percent = Column(Float)
    off_rebound = Column(Float)
    def_rebound = Column(Float)
    rebounds = Column(Float)
    assists = Column(Float)
    steals = Column(Float)
    blocks = Column(Float)
    turnovers = Column(Float)
    fouls = Column(Float)
    points = Column(Float)

    player = relationship("Player", backref=backref('stat_tables', order_by=id))
    year = relationship("Year")
    type = relationship("TableType")

Base.metadata.create_all(engine)
