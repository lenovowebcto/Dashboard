from libriarys.DB_struct import CTO_Activity
from libriarys.db_connection import session


def get_CTO_Activity_by_id(id):
    query = session.query(CTO_Activity)
    return query.get(id)

def addCTO_Activity(project):
    session.execute(CTO_Activity.__table__.insert(),project)
    session.commit()

def updateCTO_Activity(id,project):
    session.query(CTO_Activity).filter(CTO_Activity.announcement_id == id).update(project)
    session.commit()

def get_all_CTO_Activity():
    return session.query(CTO_Activity).all()

def get_CTO_Activity_by_announcement(id):
    query = session.query(CTO_Activity)
    return query.filter(CTO_Activity.announcement_id == id).all()

def get_CTO_Activity_detail(id):
    query = session.query(CTO_Activity)
    return query.get(id)
    
def create_CTO_Activity(activity):
    session.execute(CTO_Activity.__table__.insert(),activity)