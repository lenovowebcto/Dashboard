from tornado.web import authenticated
from libriarys.admin.brand import *
from libriarys.baseclass import BaseHandler
from libriarys.admin.series import get_all_series, get_series_by_id,\
    update_series, add_series

class SeriesListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Series = get_all_series()
       
        self.render('serieslist.html',series = Series)
    
class SeriesHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_series_by_id(id) 
           self.render('addseries.html',id=id,name=name,result = '')
        else :
           self.render('addseries.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('ser_name','')
        
        if int(id)>0:
            update_series(id,name)
        else :
            add_series(name)
        Series = get_all_series()
        self.render('serieslist.html',series = Series,result = 'succeeded')

