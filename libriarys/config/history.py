from libriarys.DB_struct import History
from libriarys.db_connection import session
from sqlalchemy.orm.sync import update
import datetime
now = datetime.datetime.now()  
def add_history(typeid,userid,type,update_content):
    history=History(
                    type_id=typeid,
                    userid=userid,
                    type=type,
                    update_time= now.strftime("%Y-%m-%d"),
                    update_content=update_content)
    session.add(history)
    session.commit()

if __name__ == '__main__':
#     historys = add_history("4","2","user","xiaomin")
    for history in historys:
        print(history)
        
