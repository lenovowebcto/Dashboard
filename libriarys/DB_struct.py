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
    itcode = Column(CHAR(64))
    role = Column(CHAR(64))
    department = Column(CHAR(128))
    email = Column(CHAR(64))
    password = Column(CHAR(128))
    team = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))

class Brand(BaseModel):
    __tablename__ = 'brand'

    id = Column(Integer,primary_key = True)
    name = Column(CHAR(64))

class Project(BaseModel):
    __tablename__ = 'project'

    id = Column(Integer, primary_key = True)
    name = Column(CHAR(64))
    brand = Column(CHAR(64))
    sub_seris = Column(CHAR(64))
    cot_number = Column(CHAR(64))
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
    web_cto_coumtry_scop = Column(CHAR(64))
    csr_name = Column(CHAR(64))
    por_name = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))

class Announcements(BaseModel):
    __tablename__ = 'announcements'

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

class CTO_Activity(BaseModel):
    __tablename__ = 'cto_activity'

    id = Column(Integer, primary_key = True)
    activities = Column(CHAR(64))
    owner = Column(CHAR(64))
    due_date = Column(DATE)
    start_date = Column(DATE)
    actual_comp_date = Column(DATE)

class LOIS_Activity(BaseModel):
    __tablename__ = 'lois_activity'

    id = Column(Integer, primary_key = True)
    activities = Column(CHAR(64))
    owner = Column(CHAR(64))
    due_date = Column(DATE)
    start_date = Column(DATE)
    actual_comp_date = Column(DATE)

class IAL_Activity(BaseModel):
    __tablename__ = 'ial_activity'

    id = Column(Integer, primary_key = True)
    activities = Column(CHAR(64))
    owner = Column(CHAR(64))
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

class User_history(BaseModel):
    __tablename__ = 'user_history'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(64))
    itcode = Column(CHAR(64))
    role = Column(CHAR(64))
    department = Column(CHAR(128))
    # email = Column(CHAR(64))
    # password = Column(CHAR(128))
    team = Column(CHAR(64))
    updateon = Column(DATETIME)
    updateby = Column(CHAR(64))

class Project_history(BaseModel):
    __tablename__ = 'project_history'

    id = Column(Integer, primary_key = True)
    name = Column(CHAR(64))
    brand = Column(CHAR(64))
    sub_seris = Column(CHAR(64))
    cot_number = Column(CHAR(64))
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
    web_cto_coumtry_scop = Column(CHAR(64))
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

if __name__ == '__main__':
    #init database
    init_db()