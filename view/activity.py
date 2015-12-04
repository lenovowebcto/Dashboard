from tornado.web import authenticated
from libriarys.baseclass import BaseHandler
from libriarys.activity import *


class ActivityListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        activity = get_all_Activity()
       
        self.render('activitylist.html',activity = activity)
    
class ActivityHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           act =  get_Activity_by_id(id) 
           self.render('addactivity.html',
                        id = act.id,
                        activity = act.activity,
                        team = act.team,
                        week_before_ad = act.week_before_ad,
                        week_spend = act.week_spend,
                        result = '',
                        teams = ['Web CTO','LOIS','IAL'])
        else :
           self.render('addactivity.html',
                        id = 0,
                        activity = '',
                        team = '',
                        week_before_ad = '',
                        week_spend = '',
                        result = '',
                        teams = ['Web CTO','LOIS','IAL'])           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        act = self.request.arguments
        
        if int(id)>0:
            del act['_xsrf']
            update_Activity(id,act)
        else :
            add_Activity(act)
        activity = get_all_Activity()
        self.render('activitylist.html',activity = activity,result = 'succeeded')
