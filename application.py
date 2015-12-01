#/usr/bin/env python
coding = 'utf-8'

import os
import tornado.web
from tornado.web import url
from config import debug

from view import index
from view.admin import user
from view.admin import brand
from view.admin import series
from view.admin import note

from view.admin import type
from view.admin import status
from view.admin import pro_status

from view import project
from view import announcement
from view import home

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/user/login', user.LoginHandler),
            (r'/user/logout', user.LogoutHandler),
            (r'/user/regester', user.RegesterHandler),
            (r'/brand/list', brand.BrandListHandler),
            (r'/brand/add', brand.BrandHandler),
            (r'/series/list', series.SeriesListHandler),
            (r'/series/add', series.SeriesHandler),
            (r'/type/list', type.TypeListHandler),
            (r'/type/add', type.TypeHandler),
            (r'/status/list', status.StatusListHandler),
            (r'/status/add', status.StatusHandler),
            (r'/note/list', note.NoteListHandler),
            (r'/note/add', note.NoteHandler),
            (r'/pro_status/list', pro_status.Pro_StatusListHandler),
            (r'/pro_status/add', pro_status.Pro_StatusHandler),

            (r'/admin/note/add', note.NoteHandler),
            (r'/home/', home.HomeHandler),
            
            (r'/project/index', project.ProIndexHandler),
            (r'/project/add', project.ProjectHandler),

            (r'/Announcement/add', announcement.AnnouncementHandler),
            (r'/Announcement/list', announcement.AnnouncementIndexHandler),
            (r'/Announcement/detail', announcement.AnnouncementDetail),
            (r'/Announcement/CTO', announcement.CTOHandler),
            (r'/Announcement/LOIS', announcement.LOISHandler),
            (r'/Announcement/IAL', announcement.IALHandler),
        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            cookie_secret = "dfghjklkjhgfdfghjklkjhgfertyukmncxsdertyujkn xdrtyujmn cxdfg",
           # xsrf_cookies = True,
            login_url = "/user/login",
            websitetitle='Web CTO Dashboard',
            debug =debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

application = Application()