from libriarys.DB_struct import Project, Brand
from libriarys.db_connection import session
from macpath import join

def get_all_project():
    #aa = session.query(Project,Brand.name).join(Brand,Project.brand_id==Brand.id).all()
    
    return session.query(Project,Brand).join(Brand,Project.brand_id==Brand.id).all()

    
def addproject(project):
   
    session.execute(Project.__table__.insert(),project)
    session.commit()


def get_project_by_id(id):
    query = session.query(Project)
    return query.get(id)    


def updateProject(id,project):
     session.query(id)
    