from tornado.web import RequestHandler, authenticated

class BaseHandler(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("username",self.get_argument("username"))
        self.redirect("/")

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