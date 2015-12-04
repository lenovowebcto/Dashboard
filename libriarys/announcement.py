from libriarys.DB_struct import Announcements
from libriarys.db_connection import session
from libriarys.DB_struct import Project


def get_announcement_by_id(id):
    query = session.query(Announcements)
    return query.get(id)

def addAnnouncement(announcements):
    session.execute(Announcements.__table__.insert(),announcements)
    session.commit()

def updateAnnouncement(id,announcements):
    session.query(Announcements).filter(Announcements.id == id).update(announcements)
    session.commit()

def announcement_active(id,active):
    session.query(Announcements).filter(Announcements.id == id).update({Announcements.active: active})
    session.commit()

def get_all_Announcement():
    return session.query(Announcements,Project).join(Project,Project.id==Announcements.project_id).filter(Announcements.active == 1).all()

def search_all_Announcement(brand_id, project_id, pro_type, start_AD, end_AD, status_id):
    search = "session.query(Announcements,Project).join(Project,Project.id==Announcements.project_id).filter(Announcements.active == 1"
    
    return  exec(search).all()


def get_announcement_by_project(id):
    query = session.query(Announcements)
    return query.filter(Announcements.project_id == id).all()

def get_announcement_detail(id):
    pass