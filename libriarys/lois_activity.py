from libriarys.DB_struct import LOIS_Activity
from libriarys.db_connection import session


def get_LOIS_Activity_by_id(id):
    query = session.query(LOIS_Activity)
    return query.get(id)

def addCTO_Activity(project):
    session.execute(LOIS_Activity.__table__.insert(),project)
    session.commit()

def updateLOIS_Activity(id,project):
    session.query(LOIS_Activity).filter(LOIS_Activity.announcement_id == id).update(project)
    session.commit()

def get_all_LOIS_Activity():
    return session.query(LOIS_Activity).all()

def get_LOIS_Activity_by_project(id):
    query = session.query(LOIS_Activity)
    return query.filter(LOIS_Activity.project_id == id).all()

def get_LOIS_Activity_detail(id):
    query = session.query(LOIS_Activity)
    return query.get(id)
    
def create_LOIS_Activity(activity):
    session.execute(LOIS_Activity.__table__.insert(),activity)