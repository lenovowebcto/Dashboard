from libriarys.DB_struct import Announcements, Project
from libriarys.db_connection import session
from libriarys.DB_struct import Project


def get_announcement_by_id(id):
    query = session.query(Announcements)
    return query.get(id)

<<<<<<< HEAD
def addAnnouncement(announcement):
    new = Announcements(    
                    project_id = announcement["project_id"][0],
                    sub_seris = announcement["sub_seris"][0],
#                    cto_num = announcement["cto_num"],
                    launch_type = announcement["launch_type"],
                    web_cto_ad = announcement["web_cto_ad"],
                    tables = announcement["tables"],
                    lois_ial_eow = announcement["lois_ial_eow"],
                    lois_ial_ad = announcement["lois_ial_ad"],
                    sbb_account = announcement["sbb_account"],
                    lois_mtm_account = announcement["lois_mtm_account"][0],
                    ial_mtm_account = announcement["ial_mtm_account"][0],
                    ial_no = announcement['ial_no'],
                    bpl_no = announcement['bpl_no'],
                    overall_status = announcement["overall_status"],
                    note = announcement['note'],
#                    updateon = announcement['updateon'],
#                    updateby = announcement['updateby'],
                    )
    session.add(new)
                    #    session.execute(Announcements.__table__.insert(),project)
=======
def addAnnouncement(announcements):
    session.execute(Announcements.__table__.insert(),announcements)
>>>>>>> 6e72bca5fcd6a7caa9bd6ec6dcaf9c0da1da984f
    session.commit()
    return new.id

<<<<<<< HEAD
def updateAnnouncement(id,announcement):
    session.query(Announcements).filter(Announcements.id == id).update(announcement)
    session.commit()

def get_all_Announcement():
#    return session.query(Announcements,Project).join(Project,Announcements.project_id==Project.id).all()
    return session.query(Announcements).all()
    # return session.query(Announcements,Brand).join(Brand,Project.brand_id==Brand.id).all()
=======
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

>>>>>>> 6e72bca5fcd6a7caa9bd6ec6dcaf9c0da1da984f

def get_announcement_by_project(id):
    query = session.query(Announcements)
    return query.filter(Announcements.project_id == id).all()

def get_announcement_detail(id):
    query = session.query(Announcements)
    return query.get(id)