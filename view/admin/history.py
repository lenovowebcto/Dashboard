from tornado.web import authenticated
from libriarys.config.history import *
from libriarys.baseclass import BaseHandler


class HistoryListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        History = get_all_history()  
        self.render('historylist.html',history = History)
    
class HistoryHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):    
            self.render('addhistory.html',id=0,project='',result = '')           
       



