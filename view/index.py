
from tornado.web import RequestHandler
from config import upload_dir
import os

class IndexHandler(RequestHandler):
    def get(self):
        list = os.listdir(upload_dir)
        print(self.get_secure_cookie("username"))
        print(self.get_secure_cookie("userid"))
        self.render('index.html', list=list,)
