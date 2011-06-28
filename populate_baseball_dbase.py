#! /Library/Frameworks/Python.framework/Versions/2.6/bin/python2.6

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine

from sqlalchemy.orm.exc import NoResultFound
import sys

from baseball_stats_models import YearlyBattingStats, Team, Player

import sql_alchemy_utils

from Source.Baseball_Reference_Scraping.baseball_reference import get_all_player_stats

def write_player_and_stats(session, _player, stats):

    player = Player(_player)
    session.add(player)
    session.commit()

    for stats_dict in stats:

        team_string = stats_dict['Team']
        team_query = session.query(Team).filter(Team.name == team_string)
        try:
            team = team_query.one()
        except NoResultFound:
            team = Team(team_string)
            session.add(team)
            session.commit()

        yearly_stats = YearlyBattingStats(player, team, **stats_dict)
        
        session.add(yearly_stats)
        session.commit()

def main():
    global db_password
    db_password = sys.argv[1]

    engine = sql_alchemy_utils.build_engine(db_password)
    session = sql_alchemy_utils.build_session(engine)

    for player, stats in get_all_player_stats():
        if stats: #Batters only, not getting pitchers now.
            write_player_and_stats(session, player, stats)

    return 0

if __name__ == '__main__':
    sys.exit(main())
