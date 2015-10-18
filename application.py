#/usr/bin/env python
#coding = utf8

import os
import tornado.web
from tornado.web import url

from view.index import IndexHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                    (r'/',IndexHandler),

                    ]
        settings = dict(
                        template_path = os.path.join(os.path.dirname(__file__),"templates"),
                        static_path = os.path.join(os.path.dirname(__file__),"static"),
                        websitetitle='Web CTO Dashboard',
                        debug =True,
                        )
        tornado.web.Application.__init__(self, handlers, **settings)

application = Application()