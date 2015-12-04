#run this file to create tables in database

from libriarys.db_connection import engine

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import CHAR, Integer, String, DATE, DATETIME
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)

class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(64))
    itcode = Column(CHAR(64),unique=True)
    role = Column(CHAR(64))
    department = Column(CHAR(128))
    email = Column(CHAR(64),unique=True)
    password = Column(CHAR(128))
    team = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))

class Brand(BaseModel):
    __tablename__ = 'brand'

    id = Column(Integer,primary_key = True)
    name = Column(CHAR(64),unique=True)

class Series(BaseModel):
    __tablename__ = 'config_series'

    id = Column(Integer,primary_key = True)
    ser_name = Column(CHAR(64))
    
class User_role(BaseModel):
    __tablename__ = 'config_role'

    id = Column(Integer,primary_key = True)
    role = Column(CHAR(64))   
   
class Launch_Type(BaseModel):
    __tablename__ = 'config_ltype'

    id = Column(Integer,primary_key = True)
    type = Column(CHAR(20))   
 
class Overall_Status(BaseModel):
    __tablename__ = 'config_ostatus'

    id = Column(Integer,primary_key = True)
    status = Column(CHAR(20)) 
class Note(BaseModel):
    __tablename__ = 'config_notes'

    id = Column(Integer,primary_key = True)
    note = Column(CHAR(20))  
    
class Pro_type(BaseModel):
    __tablename__ = 'config_pro_type'

    id = Column(Integer,primary_key = True)
    pro_type = Column(CHAR(20))    
class Pro_status(BaseModel):
    __tablename__ = 'config_pro_status'

    id = Column(Integer,primary_key = True)
    pro_type = Column(CHAR(20))                           
class Project(BaseModel):
    __tablename__ = 'project'

    id = Column(Integer, primary_key = True)
    name = Column(CHAR(64))
    brand_id = Column(Integer, ForeignKey('brand.id'))
    sub_seris = Column(CHAR(64))
    cto_number = Column(CHAR(64))
    ad = Column(DATE)
    eol_date = Column(DATE)
    planner = Column(CHAR(64))
    odt_lead = Column(CHAR(64))
    mkt_lead = Column(CHAR(64))
    tpm = Column(CHAR(64))
    mcs_bom = Column(CHAR(64))
    comp_bom = Column(CHAR(64))
    web_cto_pm = Column(CHAR(64))
    lois_pm = Column(CHAR(64))
    ial_pm = Column(CHAR(64))
    csr_country_scope = Column(CHAR(64))
    web_cto_country_scope = Column(CHAR(64))
    csr_name = Column(CHAR(64))
    por_name = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))
    active = Column(Integer)

class Announcements(BaseModel):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key = True)
    project_id = Column(CHAR(64))
    sub_seris = Column(CHAR(64))
    cto_num = Column(CHAR(64))
    launch_type = Column(CHAR(64))
    web_cto_ad = Column(DATE)
    tables = Column(CHAR(64))
    lois_ial_eow = Column(DATE)
    lois_ial_ad = Column(DATE)
    sbb_account = Column(CHAR(64))
    lois_mtm_account = Column(CHAR(64))
    ial_mtm_account = Column(CHAR(64))
    ial_no = Column(CHAR(64))
    bpl_no = Column(CHAR(64))
    overall_status = Column(CHAR(64))
    note = Column(CHAR(128))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))
    active = Column(Integer)

class Activity(BaseModel):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key = True)
    activity = Column(CHAR(64))
    team = Column(CHAR(64))
    week_before_ad = Column(Integer)
    week_spend = Column(Integer)
    
class CTO_Activity(BaseModel):
    __tablename__ = 'cto_activity'

    id = Column(Integer, primary_key = True)
    announcement_id = Column(Integer, ForeignKey('announcements.id'))
    activities = Column(CHAR(64))
    owner_id = Column(Integer, ForeignKey('user.id'))
    due_date = Column(DATE)
    start_date = Column(DATE)
    actual_comp_date = Column(DATE)

class LOIS_Activity(BaseModel):
    __tablename__ = 'lois_activity'

    id = Column(Integer, primary_key = True)
    announcement_id = Column(Integer, ForeignKey('announcements.id'))
    activities = Column(CHAR(64))
    owner_id = Column(Integer, ForeignKey('user.id'))
    due_date = Column(DATE)
    start_date = Column(DATE)
    actual_comp_date = Column(DATE)

class IAL_Activity(BaseModel):
    __tablename__ = 'ial_activity'

    id = Column(Integer, primary_key = True)
    announcement_id = Column(Integer, ForeignKey('announcements.id'))
    activities = Column(CHAR(64))
    owner_id = Column(Integer, ForeignKey('user.id'))
    due_date = Column(DATE)
    start_date = Column(DATE)
    actual_comp_date = Column(DATE)

class Task(BaseModel):
    __tablename__ = 'task'

    id = Column(Integer, primary_key = True)
    item = Column(CHAR(64))
    announce_id = Column(CHAR(64))
    project_name = Column(CHAR(64))
    sub_series_name = Column(CHAR(64))
    launch_type = Column(CHAR(64))
    eow = Column(DATE)
    ad = Column(DATE)
    current_activities = Column(CHAR(64))
    status = Column(CHAR(64))
    start_date = Column(DATE)
    due_date = Column(DATE)
    actual_comp_date = Column(DATE)
"""
class History(BaseModel):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    type_id = Column(CHAR(128))
    userid = Column(Integer, ForeignKey('user.id'))
    type = Column(CHAR(64))
    update_time = Column(DATE)
    update_content = Column(CHAR(128))
"""    
    
class User_history(BaseModel):
    __tablename__ = 'user_history'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(64))
    itcode = Column(CHAR(64))
    role = Column(CHAR(64))
    department = Column(CHAR(128))
    team = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))

class Project_history(BaseModel):
    __tablename__ = 'project_history'

    id = Column(Integer, primary_key = True)
    name = Column(CHAR(64))
    brand_id = Column(Integer, ForeignKey('brand.id'))
    sub_seris = Column(CHAR(64))
    cto_number = Column(CHAR(64))
    ad = Column(DATE)
    eol_date = Column(DATE)
    planner = Column(CHAR(64))
    odt_lead = Column(CHAR(64))
    mkt_lead = Column(CHAR(64))
    tpm = Column(CHAR(64))
    mcs_bom = Column(CHAR(64))
    comp_bom = Column(CHAR(64))
    web_cto_pm = Column(CHAR(64))
    lois_pm = Column(CHAR(64))
    ial_pm = Column(CHAR(64))
    csr_country_scope = Column(CHAR(64))
    web_cto_country_scope = Column(CHAR(64))
    csr_name = Column(CHAR(64))
    por_name = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))

class Announcements_history(BaseModel):
    __tablename__ = 'announcements_history'

    id = Column(Integer, primary_key = True)
    project_name = Column(CHAR(64))
    sub_seris = Column(CHAR(64))
    cto_num = Column(CHAR(64))
    launch_type = Column(CHAR(64))
    web_cto_ad = Column(DATE)
    tables = Column(CHAR(64))
    lois_ial_eow = Column(DATE)
    lois_ial_ad = Column(DATE)
    sbb_account = Column(CHAR(64))
    lois_mtm_account = Column(CHAR(64))
    ial_mtm_account = Column(CHAR(64))
    ial_no = Column(CHAR(64))
    bpl_no = Column(CHAR(64))
    overall_status = Column(CHAR(64))
    note = Column(CHAR(128))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))
    
class History(BaseModel):
    __tablename__ = 'history'  
    
    id = Column(Integer, primary_key=True)
    type_id = Column(CHAR(128))
    userid = Column(Integer, ForeignKey('user.id'))
    type = Column(CHAR(64))
    update_time = Column(DATE)
    update_content = Column(CHAR(128))



if __name__ == '__main__':
    # drop_db()
    #init database
    init_db()