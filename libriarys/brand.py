from libriarys.DB_struct import Brand
from libriarys.db_connection import session

def add_brand(brand_name):
    brand = Brand(name = brand_name)
    session.add(brand)
    session.commit()

def del_brand_by_id(id):
    query = session.query(Brand)
    brand = query.get(id)
    session.delete(brand)
    session.commit()

def update_brand(id,brand_name):
    query = session.query(Brand)
    brand = query.get(id)
    brand.name = brand_name
    session.commit()


def get_brand_by_id(id):
    query = session.query(Brand)
    return query.get(id).name

def get_all_brand():
    query = session.query(Brand)
    return query.all()

if __name__ == '__main__':
    # add_brand('zhanghc')
    # add_brand('libb')
    # add_brand('cuiyn')
    # brand = get_brand_by_id('1')
    # print(brand)
    # del_brand_by_id('1')
    # update_brand('2','guomin')
    brands = get_all_brand()
    for brand in brands:
        print(brand.name)