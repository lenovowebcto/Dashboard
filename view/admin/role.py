from tornado.web import authenticated
from libriarys.baseclass import BaseHandler
from libriarys.admin.role import *

class RoleListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Role = get_all_role()
       
        self.render('rolelist.html',role = Role)
    
class RoleHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_role_by_id(id) 
           self.render('addrole.html',id=id,name=name,result = '')
        else :
           self.render('addrole.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('role','')
        
        if int(id)>0:
            update_role(id,name)
        else :
            add_role(name)
        Role = get_all_role()
        self.render('rolelist.html',role = Role,result = 'succeeded')

