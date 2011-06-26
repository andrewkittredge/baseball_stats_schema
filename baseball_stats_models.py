#! /usr/bin/python

from sqlalchemy.ext.declaritive import declarative_base

Base = declarative_base()

class YearlyBattingStats(Base):
    __tablename__ = 'yearly_batting_stats'

    player = relationship(Player, 
                               backref=backref('__tablename__',
                               order_by=id)
                               )

    team = relationship(Team,
                        backref=backref('__tablename__',
                                        order_by=id)
                        )

class Player(Base):

    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Team(Base):

    __tablenae__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    
