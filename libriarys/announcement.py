from libriarys.DB_struct import Announcements, Project
from libriarys.db_connection import session


def get_announcement_by_id(id):
    query = session.query(Announcements)
    return query.get(id)

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
    session.commit()
    return new.id

def updateAnnouncement(id,announcement):
    session.query(Announcements).filter(Announcements.id == id).update(announcement)
    session.commit()

def get_all_Announcement():
#    return session.query(Announcements,Project).join(Project,Announcements.project_id==Project.id).all()
    return session.query(Announcements).all()
    # return session.query(Announcements,Brand).join(Brand,Project.brand_id==Brand.id).all()

def get_announcement_by_project(id):
    query = session.query(Announcements)
    return query.filter(Announcements.project_id == id).all()

def get_announcement_detail(id):
    query = session.query(Announcements)
    return query.get(id)