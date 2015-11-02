from tornado.web import RequestHandler
from libriarys.config.brand import *

class BrandHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('addbrand.html',result = '')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        add_brand(name)
        self.render('addbrand.html',result = 'save succeeded')

