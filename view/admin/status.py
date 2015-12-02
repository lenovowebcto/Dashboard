from tornado.web import authenticated
from libriarys.admin.status import *
from libriarys.baseclass import BaseHandler
# from libriarys.admin.status import *
# from libriarys.admin.series import get_all_type, get_type_by_id, update_type, add_type


class StatusListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Status = get_all_status()
       
        self.render('statuslist.html',status = Status)
    
class StatusHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_status_by_id(id) 
           self.render('addstatus.html',id=id,name=name,result = '')
        else :
           self.render('addstatus.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('status','')
        
        if int(id)>0:
            update_status(id,name)
        else :
            add_status(name)
        Status = get_all_status()
        self.render('statuslist.html',status = Status,result = 'succeeded')

