from tornado.web import authenticated
from libriarys.config.brand import *
from libriarys.baseclass import BaseHandler

class BrandHandler(BaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.render('addbrand.html',result = '')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        add_brand(name)
        self.render('addbrand.html',result = 'save succeeded')

