from tornado.web import RequestHandler
from libriarys.config.note import *

class NoteHandler(RequestHandler):

   def get(self,*args,**kwargs):
       self.render('addnote.html',result='')
       
   def post(self,*args,**kwargs):
       note = self.get_argment('note')
       add_note(note)
       self.render('note.html',result='')    