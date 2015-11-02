from tornado.web import RequestHandler
from libriarys.config.series import *

class SeriesHandler(RequestHandler):
    def get(self,*args,**kwargs):
        self.render('addseries.html',result='')
    
    def post(self,*args,**kwargs):
        name= self.get_argument('ser_name')
        add_series(name)
        self.render('addseries.html',result='')    