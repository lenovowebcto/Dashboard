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
    session.commit()

if __name__ == "__main__":
    # adduser('zhanghc','zhanghc5','pdm','cto','zhanghc5@lenovo.com','admin')
    result = login('zhanghc5','111111')
    print(result)

