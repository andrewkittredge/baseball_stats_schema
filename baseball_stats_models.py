#! /usr/bin/python

import sys

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

from sql_alchemy_utils import build_engine

Base = declarative_base()

class YearlyBattingStats(Base):
    '''Batting stats lines on baseball-reference.com.

    '''

    __tablename__ = 'yearly_batting_stats'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)

    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)

    def __init__(self, year, player):
        self.year = year
        self.player_id = player.id

class Player(Base):
    '''Baseball players.


    '''

    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    #I'm sure there are multiple baseball players with the same name,
    #not sure what the best way to avoid adding the same player twice is.
    name = Column(String(100), unique=True)

    def __init__(self, name):
        self.name = name

class Team(Base):
    '''Baseball teams.

    '''

    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, team_name):
        self.name = team_name

def load_schema():
    engine = build_engine(db_password)
    Base.metadata.create_all(engine)

def reload_schema(db_password):
    engine = build_engine(db_password)
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all(engine)

def main():
    global db_password
    db_password = sys.argv[1]
    load_schema()

    return 0

if __name__ == '__main__':
    sys.exit(main())
