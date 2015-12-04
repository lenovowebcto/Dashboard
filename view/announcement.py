from libriarys.baseclass import BaseHandler
from libriarys.announcement import *
from libriarys.activity import *
from libriarys.cto_activity import *
from libriarys.lois_activity import *
from libriarys.ial_activity import *
import datetime
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
        announcement['web_cto_ad']=datetime.datetime.strptime(str(announcement['web_cto_ad'][0],encoding='utf-8'),'%Y-%m-%d')
        announcement['lois_ial_eow']=datetime.datetime.strptime(str(announcement['lois_ial_eow'][0],encoding='utf-8'),'%Y-%m-%d')
        announcement['lois_ial_ad']=datetime.datetime.strptime(str(announcement['lois_ial_ad'][0],encoding='utf-8'),'%Y-%m-%d')
        # project = self.get_arguments('name',True)
        
            
        id = self.get_argument('id',0)
        id = int(id)
        print(announcement)
        if id>0 :
            del announcement['_xsrf']
            updateAnnouncement(id,announcement)
            ann = get_all_Announcement()
        else :
            id = addAnnouncement(announcement)
            ann = get_all_Announcement()
        activity_list = get_all_Activity()
        team_list = ['Web CTO','LOIS','IAL']
        create_activity_in_team = {'Web CTO':create_CTO_Activity, 'LOIS':create_LOIS_Activity, 'IAL':create_IAL_Activity,}
        due_date_for_team = {'Web CTO':announcement['web_cto_ad'],'LOIS':announcement['lois_ial_eow'],'IAL':announcement['lois_ial_ad'],}
        for  each in team_list:
            activitys_in_team = filter(lambda activity: activity.team == each, activity_list)
            for each_activity in activitys_in_team:
                activity = {
                'activities' : each_activity.activity,
                'announcement_id' : id,
                'due_date' : due_date_for_team[each] - datetime.timedelta(weeks = each_activity.week_before_ad),
                }
                activity['start_date'] = activity['due_date'] - datetime.timedelta(weeks = each_activity.week_spend),

                create_activity_in_team[each](activity)
        self.render('announcementlist.html',result="success",ann = ann)
        
class AnnouncementDetail(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        id = int(id)
        if id > 0 :
            ann = get_announcement_detail(id)
            cto = get_CTO_Activity_by_announcement(id)
            print(ann)
            self.render('announcementdetail.html', ann = ann)
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
        id = self.get_argument('id',0)
        cto = get_CTO_Activity_by_announcement(id)
        self.render('announcementCTO.html', activitys = cto, name = 'Web CTO')

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


