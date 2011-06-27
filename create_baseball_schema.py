#! /Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
import sys

from baseball_stats_models import YearlyBattingStats, Team, Player

import sql_alchemy_utils

def write_player_and_stats(session, player, stats):

    player = Player(player)
    session.add(player)
    session.commit()

    stats = YearlyBattingStats(2011, player)

    session.add(stats)
    session.commit()


def main():
    global db_password
    db_password = sys.argv[1]
    initialize_schema()

    return 0

if __name__ == '__main__':
    sys.exit(main())
