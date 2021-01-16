import pymysql as pm


def datacon(host, user, passwd, database):
    """
    credentials for mysql database
    """
    conn = pm.connect(host, user, passwd, database)
    return conn