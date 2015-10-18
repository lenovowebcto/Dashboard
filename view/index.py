
from tornado.web import RequestHandler
from config import upload_dir
import os

class IndexHandler(RequestHandler):
    def get(self):
        list = os.listdir(upload_dir)
        self.render('index.html',list=list)
