from libriarys.baseclass import BaseHandler
from libriarys.project import *
from libriarys.config.brand import *
class ProIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
       Pro = get_all_project()
       Pro2 = get_all_project2()
       self.render('projectlist.html',pro = Pro,Pro2 = Pro2)
        
        
class ProjectHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        id = int(id)
        brand = get_all_brand()
        if id>0 :
           pro =  get_project_by_id(id)
           self.render('addproject.html',brand = brand,project = pro,result="")
        else :
           self.render('addproject.html',brand = brand,project='',result="")
         
    def post(self, *args, **kwargs):
        project = self.request.arguments
        
        id = self.get_argument('id',0)
        id = int(id)
        
        if id>0 :
            updateProject(id,project)
        else :
            project['active'] = 1  #新加的属性
            addproject(project) 
        Pro = get_all_project()       
        self.render('projectlist.html',result="success",pro = Pro)

class ActiveHandler(BaseHandler):
      def get(self, *args, **kwargs):
          id = self.get_argument('id')
          if id>0:
              project_active(id)
          
        
        
        