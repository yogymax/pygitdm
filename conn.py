import pymysql


def get_connection(host='localhost',unm='root',pwd='root',dbnm='pydb'):
    return pymysql.connect(host,unm,pwd,dbnm)


def test_connection():
    if get_connection():
        return True
    return False

