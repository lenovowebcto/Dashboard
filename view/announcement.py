from libriarys.baseclass import BaseHandler
from libriarys.announcement import *
from libriarys.config.brand import *

# class AnnouncementIndexHandler(BaseHandler):
#     def get(self, *args, **kwargs):
#        Pro = get_all_project()
#        self.render('projectlist.html',pro = Pro)
#

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
            Ann = get_all_Announcement()
            self.render('projectlist.html',result="success",pro = Ann)
        else :
            addAnnouncement(announcement)
            Ann = get_all_Announcement()
        self.render('projectlist.html',result="success",pro = Ann)
        
        