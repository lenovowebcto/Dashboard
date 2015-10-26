#/usr/bin/env python
#coding = utf8

import os
import tornado.web
from tornado.web import url
from config import debug

from view.index import IndexHandler
from view.user import *
from view.brand import *
from view.home import HomeHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',IndexHandler),
            (r'/user/login',LoginHandler),
            (r'/user/logout',LogoutHandler),
            (r'/user/regester',RegesterHandler),
            (r'/brand/add', BrandHandler),
            (r'/home/', HomeHandler),
        ]
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            cookie_secret = "dfghjklkjhgfdfghjklkjhgfertyukmncxsdertyujkn xdrtyujmn cxdfg",
            # xsrf_cookies = True,
            login_url = "/login",
            websitetitle='Web CTO Dashboard',
            debug =debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

application = Application()