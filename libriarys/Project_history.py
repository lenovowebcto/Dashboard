from libriarys.DB_struct import  History,Project,User
from libriarys.db_connection import *


def Project_search_history(type,project_name,time1,time2):
    sql = session.query(Project.name,User.name,History.update_time,History.update_content).join(History,Project.id==History.type_id).join(User,History.userid==User.id).filter(History.type==type)
    if project_name != '':
      #  sql = sql+"and Project.name='project_name'"
       return sql.filter(Project.name==project_name)
    if time1!='':
       return sql.filter(History.update_time>=time1) 
    if time2!='':
       return sql.filter(History.update_time<=time2) 

#def Project_search_history(type,project_name,time1,time2):
#    return  session.query(Project.name,User.name,History.update_time,History.update_content).join(History,Project.id==History.type_id).join(User,History.userid==User.id).filter(History.type=='type').filter(Project.name=='project_name').filter(History.update_time>=time1).filter(History.update_time<=time2)

def Project_history(type):
  # return session.query(History).filter_by(type=1).all()
  return  session.query(Project.name,User.name,History.update_time,History.update_content).join(History,Project.id==History.type_id).join(User,History.userid==User.id).filter(History.type==type)