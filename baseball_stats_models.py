#! /usr/bin/python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class YearlyBattingStats(Base):
    '''Batting stats lines on baseball-reference.com.

    '''

    __tablename__ = 'yearly_batting_stats'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)

    player = relationship('Player', 
                               backref=backref('__tablename__',
                               order_by=id)
                               )

    team = relationship('Team',
                        backref=backref('__tablename__',
                                        order_by=id)
                        )

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
