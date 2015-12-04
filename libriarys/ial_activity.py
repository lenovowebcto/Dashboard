from libriarys.DB_struct import IAL_Activity
from libriarys.db_connection import session


def get_IAL_Activity_by_id(id):
    query = session.query(IAL_Activity)
    return query.get(id)

def addCTO_Activity(project):
    session.execute(IAL_Activity.__table__.insert(),project)
    session.commit()

def updateIAL_Activity(id,project):
    session.query(IAL_Activity).filter(IAL_Activity.announcement_id == id).update(project)
    session.commit()

def get_all_IAL_Activity():
    return session.query(IAL_Activity).all()

def get_IAL_Activity_by_project(id):
    query = session.query(IAL_Activity)
    return query.filter(IAL_Activity.project_id == id).all()

def get_IAL_Activity_detail(id):
    query = session.query(IAL_Activity)
    return query.get(id)
    
def create_IAL_Activity(activity):
    session.execute(IAL_Activity.__table__.insert(),activity)