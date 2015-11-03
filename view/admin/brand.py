from tornado.web import authenticated
from libriarys.config.brand import *
from libriarys.baseclass import BaseHandler


class BrandListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Brand = get_all_brand()
       
        self.render('brandlist.html',brand = Brand)
    
class BrandHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_brand_by_id(id) 
           self.render('addbrand.html',id=id,name=name,result = '')
        else :
           self.render('addbrand.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('name','')
        
        if int(id)>0:
            update_brand(id,name)
        else :
            add_brand(name)
        Brand = get_all_brand()
        self.render('brandlist.html',brand = Brand,result = 'succeeded')

