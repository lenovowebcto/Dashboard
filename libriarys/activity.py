from libriarys.DB_struct import Activity
from libriarys.db_connection import session

def add_Activity(activity):
    session.execute(Activity.__table__.insert(),activity)
    session.commit()

def del_Activity_by_id(id):
    query = session.query(Activity)
    Activity = query.get(id)
    session.delete(Activity)
    session.commit()

def update_Activity(id,activity):
    session.query(Activity).filter(Activity.id == id).update(activity)
    session.commit()


def get_Activity_by_id(id):
    query = session.query(Activity)
    return query.get(id)

def get_all_Activity():
    query = session.query(Activity)
    return query.all()