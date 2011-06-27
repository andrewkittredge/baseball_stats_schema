#! /Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import sys

from baseball_stats_models import YearlyBattingStats, Team, Player

def initialize_schema():
    engine = sql_alchemy_utils.create_engine()
    session = sql_alchemy_utils.build_session(engine)

    batting_stats = YearlyBattingStats(2011)

    player = Player('joe schmo')

    session.add(player)

    session.commit()

    print player.id

    batting_stats.player_id = player.id

    session.add(batting_stats)

    session.commit()


def main():
    global db_password
    db_password = sys.argv[1]
    initialize_schema()

    return 0

if __name__ == '__main__':
    sys.exit(main())
