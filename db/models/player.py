from db.setup import *

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, Sequence('player_id_seq'), primary_key=True)
    name = Column(String)
    url = Column(String)

    def __repr__(self):
        return "<Name: %s, url: %s>" % (self.name, self.url)
