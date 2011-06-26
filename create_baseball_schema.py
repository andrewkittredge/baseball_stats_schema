#! /Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import sys

DB_NAME='sql_alchemy_scratch'

ENGINE_STRING='mysql+mysqldb://root:%(db_password)s@localhost/%(db_name)s'

from baseball_stats_models import YearlyBattingStats, Team, Player

def initialize_schema():
    engine_params = {'db_password' : db_password, 'db_name' : DB_NAME}
    Session = create_engine(ENGINE_STRING % engine_params, echo=True)

    player = YearlyBattingStats('not a real player', 'red sox', 2011)


def build_batting_stats_table():
    year_column = Column('id', Integer, primary_key=True),
    age_column = Column('year', Integer),
    team_column = Column('Team', String(50)),
    league_column = Column('League', String(50)),

def main():
    global db_password
    db_password = sys.argv[1]
    initialize_schema()

    return 0

if __name__ == '__main__':
    sys.exit(main())
