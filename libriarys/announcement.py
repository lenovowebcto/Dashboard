from libriarys.DB_struct import Announcements
from libriarys.db_connection import session
from libriarys.DB_struct import Project


def get_announcement_by_id(id):
    query = session.query(Announcements)
    return query.get(id)

def addAnnouncement(project):
    session.execute(Announcements.__table__.insert(),project)
    session.commit()

def updateAnnouncement(id,project):
    session.query(Announcements).filter(Announcements.id == id).update(project)
    session.commit()

def get_all_Announcement():
    return session.query(Announcements,Project).join(Project,Project.id==Announcements.project_id).all()

def get_announcement_by_project(id):
    query = session.query(Announcements)
    return query.filter(Announcements.project_id == id).all()

def get_announcement_detail(id):
    pass