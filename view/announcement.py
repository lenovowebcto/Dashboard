from libriarys.baseclass import BaseHandler
from libriarys.announcement import *
from libriarys.config.brand import *

class AnnouncementIndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
       ann = get_all_Announcement()
       self.render('announcementlist.html',ann = ann)


class AnnouncementHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        id = int(id)
        # brand = get_all_brand()
        if id>0 :
           announcement =  get_announcement_by_id(id)
           self.render('addannounctment.html',ann = announcement)
        else :
           self.render('addannounctment.html', ann = '', result="")
         
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
        
        