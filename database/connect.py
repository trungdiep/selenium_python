#!/usr/bin/python
import psycopg2
from  database.config import config
# from configparser import ConfigParser
import json

# def config(filename=r'/home/kali/Documents/python/selenium_python/database/database.ini', section='postgresql'):
#     # create a parser
#     parser = ConfigParser()
#     # read config file
#     parser.read(filename)

#     # get section, default to postgresql
#     db = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             db[param[0]] = param[1]
#     else:
#         raise Exception(
#             'Section {0} not found in the {1} file'.format(section, filename))

#     return db


command = """
    CREATE TABLE IF NOT EXISTS baby_g (
        ID_WATCHES SERIAL ,
        category_product VARCHAR(50) ,
        introduce_product TEXT ,
        list_spec_icon TEXT[],
        price_product MONEY ,
        name_product VARCHAR(20) ,
        url_product VARCHAR(200) ,
        list_specification_product TEXT[] ,
        list_product_together_color TEXT[] ,
        new_product BOOLEAN,
        path_image VARCHAR(50)  )
    """

# def get_resource_watches(pathname="data_crawl/baby-g.json"):
#     with open(pathname,'r') as target:
#         resource_data = json.load(target)
#     for index,resource in enumerate(resource_data):
#         resource["id_watches"] = index
#     return resource_data


def  get_tuple(data):
    listvalue = list()
    for k,v in data.items():
        if k == "list_spec_icon":
            listvalue.append(list(map(lambda x: json.dumps(x), data[k])))
        else:
            listvalue.append(v)
    return tuple(listvalue)


def connect(data):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        # for resource in get_resource_watches():
        query = cur.mogrify("INSERT INTO baby_g ( {0} ) VALUES ( {1} )".format(
            ', '.join(data.keys()),
            ', '.join(['%s'] * len(data.values())),
        ), get_tuple(data))
        cur.execute(query)

        cur.execute("SELECT list_spec_icon FROM baby_g WHERE id_watches=1;")
        print(cur.fetchall())
        # for record in cur.fetchall():
        #     print(record)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Done")


if __name__ == '__main__':
    connect()
