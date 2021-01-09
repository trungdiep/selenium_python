#!/usr/bin/python
import psycopg2
# from . config import config
from configparser import ConfigParser


def config(filename=r'/home/kali/Documents/python/selenium_python/database/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db

command = """
    CREATE TABLE baby_g (
        ID_WATCHES INTEGER,
        category_product VARCHAR(50), 
        introduce_product TEXT NOT NULL, 
        price_product MONEY NOT NULL,  
        name_product VARCHAR(20) NOT NULL, 
        url_product VARCHAR(200) NOT NULL,
        list_specification_product TEXT[] NOT NULL,
        list_product_together_color TEXT[] NOT NULL,
        new_product BOOLEAN NOT NULL )
    """

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        # for command in commands:
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Donel")


if __name__ == '__main__':
    connect()
