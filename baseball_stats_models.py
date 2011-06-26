#! /usr/bin/python

import sys

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

DB_NAME='sql_alchemy_scratch'

ENGINE_STRING='mysql+mysqldb://root:%(db_password)s@localhost/%(db_name)s'

Base = declarative_base()

class YearlyBattingStats(Base):
    '''Batting stats lines on baseball-reference.com.

    '''

    __tablename__ = 'yearly_batting_stats'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)

    player_id = Column(Integer, ForeignKey('players.id'))

    team_id = Column(Integer, ForeignKey('teams.id'))

    def __init__(self, player, team, year):
        self.year = year
        self.team = team
        self.player = player

class Player(Base):
    '''Baseball players.


    '''

    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Team(Base):
    '''Baseball teams.

    '''

    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


def load_schema():
    engine_params = {'db_password' : db_password, 'db_name' : DB_NAME}
    engine = create_engine(ENGINE_STRING % engine_params, echo=True)
    Base.metadata.create_all(engine)

def main():
    global db_password
    db_password = sys.argv[1]
    load_schema()

    return 0

if __name__ == '__main__':
    sys.exit(main())
