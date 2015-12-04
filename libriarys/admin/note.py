from libriarys.DB_struct import  Note
from libriarys.db_connection import session

def add_note(note_name):
    note = Note(note = note_name)
    session.add(note)
    session.commit()

def del_note_by_id(id):
    query = session.query(Note)
    note = query.get(id)
    session.delete(note)
    session.commit()

def update_note(id,note_name):
    query = session.query(Note)
    note = query.get(id)
    note.note = note_name
    session.commit()


def get_note_by_id(id):
    query = session.query(Note)
    return query.get(id).note

def get_all_note():
    query = session.query(Note)
    return query.all()

if __name__ == '__main__':
   
    types = get_all_note()
    for note in notes:
        print(note.name)