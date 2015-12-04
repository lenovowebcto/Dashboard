from libriarys.DB_struct import  Launch_Type
from libriarys.db_connection import session

def add_type(type_name):
    typ = Launch_Type(type = type_name)
    session.add(typ)
    session.commit()

def del_type_by_id(id):
    query = session.query(Launch_Type)
    type = query.get(id)
    session.delete(type)
    session.commit()

def update_type(id,type_name):
    query = session.query(Launch_Type)
    type = query.get(id)
    type.type = type_name
    session.commit()


def get_type_by_id(id):
    query = session.query(Launch_Type)
    return query.get(id).type

def get_all_type():
    query = session.query(Launch_Type)
    return query.all()

if __name__ == '__main__':
   
    types = get_all_type()
    for type in types:
        print(type.name)