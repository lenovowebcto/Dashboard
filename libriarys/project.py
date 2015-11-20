from libriarys.DB_struct import Project, Brand
from libriarys.db_connection import session
from macpath import join

def get_all_project():
    return session.query(Project,Brand).join(Brand,Project.brand_id==Brand.id).filter(Project.active == 1).all()

def get_all_project2():
    return session.query(Project,Brand).join(Brand,Project.brand_id==Brand.id).filter(Project.active == 0).all()

def get_all():
    return session.query(Project).all()
    
def addproject(project):
   
    session.execute(Project.__table__.insert(),project)
    session.commit()


def get_project_by_id(id):
    query = session.query(Project)
    return query.get(id)    


def updateProject(id,project):
    session.query(Project).filter(Project.id == id).update(project)
    session.commit()
    
def project_active(id):
    #session.delete()    
    pass
   