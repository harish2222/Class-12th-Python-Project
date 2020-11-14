from data_analyse import data_analyse_menu, maxima
import pandas as pd 
import matplotlib.pyplot as plt
import psycopg2 as pc
from conn import *

def wel():
    """
    This is a welcome script
    """
    print("|=====================================Welcome TO HK TRENDS======================================|")

def maincode():
    
    """
    Main menu is given here
    """
    
    db = dbconn("googletrends_data","postgres","postgresql")
    cur = db.cursor()
    
    
    
    print("\n\t\tEnter--1--Print raw data in console\n")                                                                          
                                                                                                                     
    print("\t\tEnter--2--Show Graphical Data\n")

    print("\t\tEnter--3--Show DATA From Postgresql\n")                                                                          
                                                                                                                     
    print("\t\tEnter--4--Show Raw Data from Postgresql\n")                                                                      
                                                                                                                     
    print("\t\tEnter--5--Show DATA from CSV\n")                                                                                 
                                                                                                                     
    print("\t\tEnter--6--Data Analysis\n")                                                                                      
                                                                                                                     
    print("\t\tEnter--7--Exit\n")

    



    usr_input = int(input("Enter the Number :\t"))

    if usr_input==1:
        cur.execute("select * from programming_language.coding;")
        row = cur.fetchall()
        print(row)
        maincode()

    elif usr_input==2:
        data_visual()


    elif usr_input==3:
        df = dict()
        w = list()
        k = list()
        j = list()
        p = list()
        c = list()

        js = list()
        cur.execute("select * from programming_language.coding;")
        row = cur.fetchall()
        for r in row:
            
            w.append(f"{r[0]}")
            k.append(f"{r[1]}")
            j.append(f"{r[2]}")
            p.append(f"{r[3]}")
            c.append(f"{r[4]}")
            js.append(f"{r[5]}")

        df = {"WEEK":w,"KOTLIN":k,"JAVA":j,"PYTHON":p,"C++":c,"JAVASCRIPT":js}
        c = pd.DataFrame(df)
        print(c)
        maincode()

    elif usr_input==4:
        w = list()
        k = list()
        j = list()
        p = list()
        c = list()
        js = list()
        t = list()
        cur.execute("select * from programming_language.coding;")
        row = cur.fetchall()
        for r in row:
            
            w.append(f"{r[0]}")
            k.append(f"{r[1]}")
            j.append(f"{r[2]}")
            p.append(f"{r[3]}")
            c.append(f"{r[4]}")
            js.append(f"{r[5]}")
        t.append(w)
        t.append(k)
        t.append(j)
        t.append(p)
        t.append(c)
        t.append(js)    
        print(t)
        maincode()

    elif usr_input==5:
        csv_data = pd.read_csv("H:\PROGRAMMING\PYTHON\Class 12th Python Project\csv_data\kjpcjs.csv")
        print(csv_data)
        maincode()
    elif usr_input==6:
        data_analyse_menu()
        maincode()

    elif usr_input==7:
        exit()

                
    db.close()
if __name__=='__main__':
    wel()
    maincode()
