#/usr/bin/env python
#coding:utf8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from application import application

from tornado.options import define, options
define("port", default = 8001, help = "run on the given port",type = int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(tornado.options.options.port)
#     http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()