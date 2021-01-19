from conn import *
from data_analyse import data_analyse_menu
import pymysql as pms
from mysqlcon import datacon
import getpass
import pandas as pd


def wel():
    """
    This is a welcome script
    """

    print("|=====================================Welcome TO HK TRENDS======================================|")


# noinspection PyShadowingNames
def maincode(dbs, usr, pswd):
    """
    Main menu is given here
    with Mainly postgres and other csv action
    """
    sc = "SELECT * FROM programming_languages.kpjsc;"

    db = dbconn(dbs, usr, pswd)

    cur = db.cursor()

    print("\t\tEnter--2--Show Graphical Data\n")

    print("\t\tEnter--5--Show DATA from CSV\n")

    print("\t\tEnter--6--Data Analysis\n")

    print("\t\tEnter--3--Show DATA From Postgresql\n")

    print("\t\tEnter--7--Exit\n")

    usr_input = int(input("Enter the Number :\t"))

    if usr_input == 2:
        data_visual()

    if usr_input == 3:

        w = list()
        k = list()
        j = list()
        p = list()
        c = list()

        js = list()
        sc = "SELECT * FROM programming_languages.kpjsc;"
        cur.execute(sc)
        row = cur.fetchall()
        for r in row:
            w.append(f"{r[0]}")
            k.append(f"{r[1]}")
            j.append(f"{r[2]}")
            p.append(f"{r[3]}")
            c.append(f"{r[4]}")
            js.append(f"{r[5]}")

        df = {"WEEK": w, "KOTLIN": k, "JAVA": j,
              "PYTHON": p, "C++": c, "JAVASCRIPT": js}
        c = pd.DataFrame(df)
        print(c)
        maincode(datab, usr, pswd)


    elif usr_input == 5:
        csv_data = pd.read_csv(
            "kjpcjs.csv")
        print(csv_data)
        maincode(datab, usr, pswd)
    elif usr_input == 6:
        data_analyse_menu()
        maincode(datab, usr, pswd)

    elif usr_input == 7:
        exit()
    db.close()


# noinspection PyGlobalUndefined
def mysql_runned_maincode(host, user, passwd, database):
    global mysqlcon
    try:
        mysqlcon = datacon(host, user, passwd, database)
    except:
        var = pms.MySQLError
        print(var)

    print(mysqlcon)
    cur = mysqlcon.cursor()

    print("\t\n1.Mysql Raw Data")
    print("\t\n2.Mysql Structure Data")
    print("\t\n3.Exit")

    usr_input = int(input("Enter the index:\t"))

    if usr_input == 1:
        query = str(input("Enter your query:\t"))
        cur.execute(query)
        row = cur.fetchall()
        print(row)
        mysql_runned_maincode(host, user, passwd, database)

    elif usr_input == 2:
        query = str(input("Enter The query:\t"))
        cur.execute(query)
        w = list()
        k = list()
        j = list()
        p = list()
        c = list()
        js = list()
        row = cur.fetchall()
        for r in row:
            w.append(f"{r[0]}")
            k.append(f"{r[1]}")
            j.append(f"{r[2]}")
            p.append(f"{r[3]}")
            c.append(f"{r[4]}")
            js.append(f"{r[5]}")

        df = {"WEEK": w, "KOTLIN": k, "JAVA": j,
              "PYTHON": p, "C++": c, "JAVASCRIPT": js}
        c = pd.DataFrame(df)
        print(c)
        mysql_runned_maincode(host, user, passwd, database)

    if usr_input == 3:
        exit()

    mysqlcon.close()


if __name__ == '__main__':
    print("\tWhich DataBase Connectivity do you Want\n")
    print("\t1.Mysql\n")
    print("\t2.Postgresql\n")
    print("\t3.Csv Data\n")
    input_data = int(input("Enter the index of the databse Menu:\t"))
    if input_data == 1:
        host = str(input("Enter hosting address:\t"))
        database = str(input("Enter the database name:\t"))
        user = str(input("Enter user crendentials:\t"))
        passwd = str(getpass.getpass("Enter user Password"))
        mysql_runned_maincode(host, user, passwd, database)
    elif input_data == 2:
        datab = str(input("Enter the database name:\t"))
        usr = str(input("Enter user crendentials:\t"))
        pswd = str(getpass.getpass("Enter user Password"))
        wel()
        maincode(datab, usr, pswd)
    elif input_data == 3:
        pass
