from libriarys.baseclass import BaseHandler
from libriarys.announcement import *
from libriarys.admin import brand
from libriarys import project
from libriarys.admin import type
from libriarys.admin import status


class AnnouncementIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
       ann = get_all_Announcement()
       pr = project.get_all()
       br = brand.get_all_brand()
       ty = type.get_all_type()
       st = status.get_all_status()
       self.render('announcementlist.html',ann = ann,project = pr, brand = br, type = ty,status = st)

    def post(self):
        brand_id = self.get_argument('brand', '')
        project_id = self.get_argument('project', '')
        pro_type = self.get_argument('pro_type', '')
        start_AD = self.get_argument('start_AD', '')
        end_AD = self.get_argument('end_AD', '')
        status_id = self.get_argument('status', '')
        
        ann = search_all_Announcement(brand_id, project_id, pro_type, start_AD, end_AD, status_id)
        pr = project.get_all()
        br = brand.get_all_brand()
        ty = type.get_all_type()
        st = status.get_all_status()
        self.render('announcementlist.html',ann = ann,project = pr, brand = br, type = ty,status = st)


class AnnouncementHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        id = int(id)
        pro = project.get_all()
        if id>0 :
           announcement =  get_announcement_by_id(id)
           self.render('addannounctment.html',pro = pro, ann = announcement)
        else :
           self.render('addannounctment.html', pro = pro, ann = '', result="")
         
    def post(self, *args, **kwargs):
        announcement = self.request.arguments
        # project = self.get_arguments('name',True)
        id = self.get_argument('id',0)
        id = int(id)
        # print(announcement)
        if id>0 :
            del announcement['_xsrf']
            updateAnnouncement(id,announcement)
            ann = get_all_Announcement()
            self.render('announcementlist.html',result="success",ann = ann)
        else :
            addAnnouncement(announcement)
            ann = get_all_Announcement()
        self.render('announcementlist.html',result="success",ann = ann)
        
class AnnouncementDetail(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        id = int(id)
        if id > 0 :
            ann = get_announcement_detail(id)
            self.render('announcementdetail.html')
        else:
            self.render('announcementlist.html')

class ActiveHandler(BaseHandler):
      def get(self, *args, **kwargs):
          id = self.get_argument('id')
          active = self.get_argument('active')
          announcement_active(id,active)
          self.redirect('/Announcement/list') 

class CTOHandler(BaseHandler):
    def get(self, *args, **kwargs):

        self.render('announcementCTO.html')

    def post(self, *args, **kwargs):
        pass

class IALHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

class LOISHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass


