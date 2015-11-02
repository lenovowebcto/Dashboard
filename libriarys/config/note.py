'''
Created on 2015Äê10ÔÂ22ÈÕ

@author: libb4
'''

from libriarys.DB_struct import Note
from libriarys.db_connection import session

def add_note(note):
    note = Note(note=note)
    session.add(note)
    session.commit()
    
    
    