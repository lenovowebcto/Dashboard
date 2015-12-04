from libriarys.DB_struct import  Overall_Status
from libriarys.db_connection import session

def add_status(status_name):
    sta = Overall_Status(status = status_name)
    session.add(sta)
    session.commit()

def del_status_by_id(id):
    query = session.query(Overall_Status)
    status = query.get(id)
    session.delete(status)
    session.commit()

def update_status(id,status_name):
    query = session.query(Overall_Status)
    status = query.get(id)
    status.status = status_name
    session.commit()


def get_status_by_id(id):
    query = session.query(Overall_Status)
    return query.get(id).status

def get_all_status():
    query = session.query(Overall_Status)
    return query.all()

if __name__ == '__main__':
   
    types = get_all_status()
    for status in statuss:
        print(status.name)