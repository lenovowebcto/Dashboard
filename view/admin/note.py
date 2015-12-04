from tornado.web import authenticated
from libriarys.admin.note import *
from libriarys.baseclass import BaseHandler
# from libriarys.admin.status import *
# from libriarys.admin.series import get_all_type, get_type_by_id, update_type, add_type


class NoteListHandler(BaseHandler):
    #@authenticated
    def get(self, *args, **kwargs):
        Note = get_all_note()
       
        self.render('notelist.html',note = Note)
    
class NoteHandler(BaseHandler):
#     @authenticated
    def get(self, *args, **kwargs):
        
        id = self.get_argument('id',0)
        id = int(id)
        if id>0 :
           name =  get_note_by_id(id) 
           self.render('addnote.html',id=id,name=name,result = '')
        else :
           self.render('addnote.html',id=0,name='',result = '')           
       

    def post(self, *args, **kwargs):
        id = self.get_argument('id',0)
        name = self.get_argument('note','')
        
        if int(id)>0:
            update_note(id,name)
        else :
            add_note(name)
        Note = get_all_note()
        self.render('notelist.html',note = Note,result = 'succeeded')

