#! /usr/bin/python

from sqlalchemy import create_engine

ENGINE_STRING='mysql+mysqldb://root:%(db_password)s@localhost/%(db_name)s'
DB_NAME='sql_alchemy_scratch'

from sqlalchemy.orm import sessionmaker

def build_engine(db_password):
    engine_params = {'db_password' : db_password, 'db_name' : DB_NAME}
    engine = create_engine(ENGINE_STRING % engine_params, echo=True)
    return engine

def build_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
