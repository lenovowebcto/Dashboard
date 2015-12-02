from tornado.web import authenticated
from libriarys.admin.pro_status import *
from libriarys.baseclass import BaseHandler
# from libriarys.admin.status import *
# from libriarys.admin.series import get_all_type, get_type_by_id, update_type, add_type


class Pro_StatusListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Status = get_all_prostatus()
       
        self.render('pro_statuslist.html',pro_type = Status)
    
class Pro_StatusHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_prostatus_by_id(id) 
           self.render('addpro_status.html',id=id,name=name,result = '')
        else :
           self.render('addpro_status.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('pro_type','')
        
        if int(id)>0:
            update_prostatus(id,name)
        else :
            add_prostatus(name)
        Status = get_all_prostatus()
        self.render('pro_statuslist.html',pro_type = Status,result = 'succeeded')

