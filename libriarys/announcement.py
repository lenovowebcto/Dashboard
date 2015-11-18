from libriarys.DB_struct import Announcements
from libriarys.db_connection import session


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
    return session.query(Announcements).all()
    # return session.query(Announcements,Brand).join(Brand,Project.brand_id==Brand.id).all()

def get_announcement_by_project(id):
    query = session.query(Announcements)
    return query.filter(Announcements.project_id == id).all()

