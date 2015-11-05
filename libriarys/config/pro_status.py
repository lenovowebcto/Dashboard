from libriarys.DB_struct import  Pro_status
from libriarys.db_connection import session

def add_prostatus(status_name):
    sta = Pro_status(pro_type = status_name)
    session.add(sta)
    session.commit()

def del_prostatus_by_id(id):
    query = session.query(Pro_status)
    pro_type = query.get(id)
    session.delete(pro_type)
    session.commit()

def update_prostatus(id,status_name):
    query = session.query(Pro_status)
    pro_type = query.get(id)
    pro_type.pro_type = status_name
    session.commit()


def get_prostatus_by_id(id):
    query = session.query(Pro_status)
    return query.get(id).pro_type

def get_all_prostatus():
    query = session.query(Pro_status)
    return query.all()

if __name__ == '__main__':
   
    pro_types = get_all_status()
    for pro_type in pro_types:
        print(pro_type.name)