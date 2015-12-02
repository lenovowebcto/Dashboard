from libriarys.DB_struct import  User_role
from libriarys.db_connection import session

def add_role(name):
    rol = User_role(role = name)
    session.add(rol)
    session.commit()

def del_role_by_id(id):
    query = session.query(User_role)
    role = query.get(id)
    session.delete(role)
    session.commit()

def update_role(id,role):
    query = session.query(User_role)
    roles = query.get(id)
    roles.role = role
    session.commit()


def get_role_by_id(id):
    query = session.query(User_role)
    return query.get(id).role

def get_all_role():
    query = session.query(User_role)
    return query.all()

if __name__ == '__main__':
   
    roles = get_all_role()
    for role in roles:
        print(role.name)