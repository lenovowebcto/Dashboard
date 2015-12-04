from tornado.web import authenticated
from libriarys.user import *
from libriarys.user import login
from libriarys.baseclass import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', warning = '')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        result,user = login(username,password)
        if result:
            self.set_secure_cookie("username",str(username),expires_days=None)
            self.set_secure_cookie("userid",str(user.id),expires_days=None)
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
 
#    ҳ���߼���ʼ 
class UserListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        User = get_all_User()   
        self.render('userlist.html',pro = User)

        
class UserHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_argument('id',0)
        dele = self.get_argument('del',"0")
        id = int(id)
        # brand = get_all_brand()
        #ɾ������
        if dele == "1":
            deleteUser(id)
            Ann = get_all_User()
            self.render('userlist.html',result="success",pro = Ann)
        #�޸�ҳ��
        if id>0 :
            user =  get_user_by_id(id)
            self.render('adduser.html',warning = '', ann = user)
        #���ҳ��
        else :
            self.render('adduser.html', ann = '', warning = '')
                   
    def post(self, *args, **kwargs):
        user = self.request.arguments
        id = self.get_argument('id',0)
        id = int(id)
        
        #�޸Ĳ���
        if id>0 :
            if user['password'] == user['confpassword']:
                del user['_xsrf']
                del user['confpassword']
                updateUser(id,user)
                Ann = get_all_User()
                self.render('userlist.html',result="success",pro = Ann)
            else:
                del user['_xsrf']
                user =  get_user_by_id(id)
                self.render('adduser.html',ann = user ,warning = 'Password false.Please check your password.')                  
        #��Ӳ���
        else :
            if user['password'] == user['confpassword']:
                del user['_xsrf']
                del user['confpassword']
                addUser(user)
                Ann = get_all_User()
                self.render('userlist.html',result="success",pro = Ann)
            else:
                self.render('adduser.html',ann = '', warning = 'Password false.Please check your password.')
        
        
        