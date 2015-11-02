#/usr/bin/env python
coding = 'utf-8'

import os
import tornado.web
from tornado.web import url
from config import debug

from view.index import IndexHandler
from view.user import *
from view.brand import *
<<<<<<< HEAD
from view.admin.note import *
from view.config.series import *

=======
from view.home import HomeHandler
>>>>>>> ca83cf27b263ddb7c75b660d0e78e3a3166a2dd6

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',IndexHandler),
            (r'/user/login',LoginHandler),
            (r'/user/logout',LogoutHandler),
            (r'/user/regester',RegesterHandler),
            (r'/brand/add', BrandHandler),
<<<<<<< HEAD
            (r'/config/series/add', SeriesHandler),
            (r'/admin/note/add', NoteHandler),
=======
            (r'/home/', HomeHandler),
>>>>>>> ca83cf27b263ddb7c75b660d0e78e3a3166a2dd6
        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            cookie_secret = "dfghjklkjhgfdfghjklkjhgfertyukmncxsdertyujkn xdrtyujmn cxdfg",
            #xsrf_cookies = True,
            login_url = "/login",
            websitetitle='Web CTO Dashboard',
            debug =debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

application = Application()