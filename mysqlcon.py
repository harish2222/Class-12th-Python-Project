import pymysql as pm

def datacon(host,user,passwd,database):
    """
    credentials for mysql database
    """
    conn = pm.connect(host,user,passwd,database)
    cur = conn.cursor()
    cur.execute("SELECT * from google_trends;")
