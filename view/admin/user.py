from tornado.web import authenticated
from libriarys.user import login
from libriarys.baseclass import BaseHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', warning = '')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        result = login(username,password)
        if result:
            self.set_secure_cookie("username",str(username))
            self.redirect("/")
        else:
            self.render('login.html',warning = 'Login false.Please check your itcode and password.')

class WelcomeHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render('index.html',user = self.current_user)

class LogoutHandler(BaseHandler):
    def get(self):
        if(self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.redirect("/")

class RegesterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass