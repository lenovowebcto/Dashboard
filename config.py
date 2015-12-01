#!/usr/bin/env python
# encoding: utf-8

import os

#database config
host = 'localhost'
# host = '192.168.27.196'
db_port = 3306
user = 'root'

dbname = 'dashboard'
password = '123456'

debug = True
default_user_password = '111111'

if os.name =='nt':
    upload_dir = os.getcwd()+"\\static\\image\\upload\\"
else :
    upload_dir = os.getcwd()+"/static/image/upload/"
    
  

    
