#! /usr/bin/python

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

import baseball_reference

def create_tables():
    metadata = MetaData()    


def build_batting_stats_table():
    year_column = Column('id', Integer, primary_key=True),
    age_column = Column('year', Integer),
    team_column = Column('Team', String(50)),
    league_column = Column('League', String(50)),
    
