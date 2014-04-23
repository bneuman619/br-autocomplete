import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine('sqlite:///player_db.db', echo=True)
Base = declarative_base()
Session = sqlalchemy.orm.sessionmaker(bind=engine)
