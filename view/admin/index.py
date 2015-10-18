#/usr/bin/env python
#coding = utf8

from tornado.web import RequestHandler
from config import upload_dir
import os

class AdminHandler(RequestHandler):
    def get(self):
        list = os.listdir(upload_dir)
        self.render('admin/index.html',list=list[:4])
