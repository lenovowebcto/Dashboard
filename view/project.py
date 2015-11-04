from libriarys.baseclass import BaseHandler
from libriarys.project import *
from libriarys.config.brand import *
class ProIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
       Pro = get_all_project()
       self.render('projectlist.html',pro = Pro)
        
        
class ProjectHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        id = int(id)
        brand = get_all_brand()
        if id>0 :
           pro =  get_project_by_id(id)
           self.render('addproject.html',brand = brand,project = pro,result="")
        else :
           self.render('addproject.html',brand = brand,result="")
        
       
      
    def post(self, *args, **kwargs):
        project = self.request.arguments
        
#         project = self.get_arguments('name',True)
        id = self.get_argument('id',0)
        id = int(id)
        
        if id>0 :
            updateProject(id,project)
        else :
            addproject(project) 
        Pro = get_all_project()       
        self.render('projectlist.html',result="success",pro = Pro)
        
        