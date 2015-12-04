from config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import pymysql
#
# #connect DB by pymysql
# db = pymysql.connect(database=dbname,
#                      user=user,
#                      password=password,
#                      host=host,
#                      port=db_port,
#                      use_unicode=True,
#                      charset="utf8",
#                      cursorclass = pymysql.cursors.DictCursor
#                      )

#connect DB by SQLalchemy

DB_CONNECT_STRING = 'mysql+pymysql://'+user+':'+password+'@'+host+'/'+dbname+'?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=debug)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

if __name__ == '__main__':
    pass
