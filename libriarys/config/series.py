from libriarys.DB_struct import  Series
from libriarys.db_connection import session

def add_series(name):
    ser = Series(ser_name = name)
    session.add(ser)
    session.commit()

def del_series_by_id(id):
    query = session.query(Series)
    series = query.get(id)
    session.delete(series)
    session.commit()

def update_series(id,ser_name):
    query = session.query(Series)
    series = query.get(id)
    series.name = series_name
    session.commit()


def get_series_by_id(id):
    query = session.query(series)
    return query.get(id).name

def get_all_series():
    query = session.query(series)
    return query.all()

if __name__ == '__main__':
   
    seriess = get_all_series()
    for series in seriess:
        print(series.name)