from libriarys.baseclass import BaseHandler
from libriarys.project import *
from libriarys.admin.brand import *
from libriarys.Project_history import *
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
            project['active'] = 1  
            addproject(project) 

        Pro = get_all_project()  
        Pro2 = get_all_project2()     
        self.render('projectlist.html',result="success",pro = Pro,Pro2 = Pro2)

class ActiveHandler(BaseHandler):
      def get(self, *args, **kwargs):
          id = self.get_argument('id')
          active = self.get_argument('active')
          project_active(id,active)
          self.redirect('/project/index') 


class ProQuyHandler(BaseHandler):   
      def get(self, *args, **kwargs):
          type="project"
          ph =  Project_history(type)
         
          self.render('project_history.html',result = ph,project_name='',time1='',time2='')
      
      def post(self,*args, **kwargs): 
          project_name = self.get_argument('project_name')
          time1 = self.get_argument('time1')
          time2 = self.get_argument('time2')
          type="project"
          ph =  Project_search_history(type,project_name,time1,time2)
          self.render('project_history.html',result = ph,project_name=project_name,time1=time1,time2=time2)
          
             
