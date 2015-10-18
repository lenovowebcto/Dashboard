# /usr/bin/env python
# coding=utf-8

import pymysql
from config import *

db = pymysql.connect(database=dbname, 
                     user=user, 
                     password=password, 
                     host=host, 
                     port=db_port, 
                     use_unicode=True, 
                     charset="utf8",
                     cursorclass = pymysql.cursors.DictCursor
                     )

if __name__ == '__main__':
    pass
