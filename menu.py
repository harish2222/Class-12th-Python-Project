from conn import *
from data_analyse import data_analyse_menu

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

    

    print("\t\tEnter--1--Show DATA From Postgresql\n")

    print("\t\tEnter--2--Exit\n")

    usr_input = int(input("Enter the Number :\t"))

    if usr_input == 1:

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

    elif usr_input == 2:
        exit()
    db.close()


if __name__ == '__main__':
    print("\tWhich DataBase Connectivity do you Want\n")
    print("\t1.Postgresql\n")
    print("\t2.Csv Data\n")
    print("\t3.Grphical Representation\n")
    print("\t4.Data Analysis\n")
    print("\t5.Exit\n")
    input_data = int(input("Enter the index of the databse Menu:\t"))
    if input_data == 1:
        datab = str(input("Enter the database name:\t"))
        usr = str(input("Enter user crendentials:\t"))
        pswd = str(input("Enter user Password"))
        wel()
        maincode(datab, usr, pswd)
    elif input_data == 2:
        csv_data = pd.read_csv("kjpcjs.csv")
        print(csv_data)
    elif input_data == 3:
        data_visual()
    elif input_data == 4:
        data_analyse_menu()
    elif input_data == 5:
        exit()
    else:
        exit()
