from libriarys.baseclass import BaseHandler
from libriarys.announcement import *
from libriarys.admin.brand import *
from libriarys import project

class AnnouncementIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
       ann = get_all_Announcement()
       self.render('announcementlist.html',ann = ann)


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


