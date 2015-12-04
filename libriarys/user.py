from libriarys.DB_struct import User_history
from libriarys.DB_struct import User
from libriarys.db_connection import session
from libriarys.commonfunction import md5
from config import default_user_password

def adduser(username,itcode,department,team,email,role):
    user = User(name = username,
                role = role,
                itcode = itcode,
                department = department,
                team = team,
                email = email,
                password = md5(default_user_password))
    session.add(user)
    session.flush()
    session.commit()

def login(itcode,password):
    query = session.query(User)
    user = query.filter_by(itcode = itcode).first()
    if user :
        db_password = user.password
        print(db_password)
        if md5(password) == db_password:
            return True
        else:
            return False
    else:
        return False

def adduser_by_dic(user):
    session.execute(User.__table__.insert(),user)
#     session.execute(User_history.__table__.insert(),user)
    session.commit()

if __name__ == "__main__":
    # adduser('zhanghc','zhanghc5','pdm','cto','zhanghc5@lenovo.com','admin')
    result = login('zhanghc5','111111')
    print(result)

# Ò³ÃæÂß¼­¿ªÊ¼
def get_user_by_id(id):
    query = session.query(User)
#     query.filter(User.id == id).delete()
    return query.get(id)

def addUser(user):
    
    session.execute(User.__table__.insert(),user)
    session.execute(User_history.__table__.insert(),user)
    session.commit()
    
def deleteUser(id):
    query = session.query(User)
    query.filter(User.id == id).delete()
    session.commit()

def updateUser(id,project):
    session.query(User).filter(User.id == id).update(project)
    session.commit()

def get_all_User():
    query = session.query(User)
    return query.all()

def get_user_by_project(id):
    query = session.query(User)
    return query.filter(User.project_id == id).all()





