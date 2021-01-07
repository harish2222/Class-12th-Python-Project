import pymysql as pm

def datacon(host,user,passwd,database):
    """
    credentials for mysql database
    """
    conn = pm.connect(host,user,passwd,database)
    cur = conn.cursor()
    cur.execute("SELECT * from google_trends;")
    r = cur.fetchall()
    for i in r:
        print(f"{i[0]}")
if __name__ == "__main__":
    datacon("localhost","root",'mysql','google_trends')