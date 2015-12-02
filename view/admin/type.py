from tornado.web import authenticated
from libriarys.admin.type import *
from libriarys.baseclass import BaseHandler
# from libriarys.admin.type import *
# from libriarys.admin.series import get_all_type, get_type_by_id, update_type, add_type


class TypeListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Type = get_all_type()
       
        self.render('typelist.html',type = Type)
    
class TypeHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_type_by_id(id) 
           self.render('addtype.html',id=id,name=name,result = '')
        else :
           self.render('addtype.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('type','')
        
        if int(id)>0:
            update_type(id,name)
        else :
            add_type(name)
        Type = get_all_type()
        self.render('typelist.html',type = Type,result = 'succeeded')

