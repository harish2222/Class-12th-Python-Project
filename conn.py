import psycopg2 as pc
import pandas as pd
import matplotlib.pyplot as mp

from graphs import * 
from menu import maincode



def dbconn(db, usr, pswd):
    dbc = pc.connect(host="localhost", database=db, user=usr, password=pswd)
    return dbc


# def mysql_conn(parameter_list):
#     """
#     this module is for mysql connectivity 
#     """
#     mydb = mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "mysql",
#         database = "google_trends",
#         port = 3306
#     )

def data_visual():
    """
    calling the sub menu of the graph option . 
    The menu as follows:\n
    1.Show DATA In Line Graph\n
    2.Show DATA in Scatter Graph\n
    3.Show DATA in Dotted Graph\n
    4.Show DATA in Bar Graph\n
    5.Show DATA in Shape Graph\n
    6.Show DATA in Histograph\n
    7.Show DATA in Pie Chart\n
    With user_input in it for the sno numbers of the menu\n
    user_input = int(input("Enter the index value of the following choices:"))
    """
    print("|================GRAPHICAL REPRESENTATION===============|")
    print("\n\t\t1.Show DATA In Line Graph\n")
    print("\t\t2.Show DATA in Splitted Line Graph\n")
    print("\t\t3.Show DATA in Nested Pie Chart \n")
    print("\t\t4.Show DATA in Bar Graph\n")
    print("\t\t5.Show DATA in Splitted Bar Graphs\n")
    print("\t\t6.Show DATA in Splitted Pie Chart\n")
    print("\t\t7.Show DATA in Pie Chart\n")
    print("\t\t8.EXIT\n")


    user_input = int(input("Enter the index value of the following choices:"))

    if user_input == 1:  # |here we will plot a line graph|
        linegraph()
        data_visual()
            
                        

    elif user_input == 2:  # |plotting a scatter graph|
        splitlinegraph()
        data_visual()


    elif user_input == 3:  # |plotting a dotted graph|
        data_visual()


    elif user_input == 4:  # |plotting a Bar graph|
        bargraph()
        data_visual()

    elif user_input == 5:  # |Splitted Bar graphs|
        bargraphs()
        data_visual()

    elif user_input == 6:  # |Splitted Piecharts|
        splitted_piecharts()
        data_visual()

    elif user_input == 7:  # |Piechart|
        piecharts()
        data_visual()

    elif user_input ==8:
        exit()
        
    

    elif user_input == "Null":
        print("Invalid request")
        data_visual()
        

    elif user_input == "":
        print("Invalid request")
        data_visual()   

    else:
        exit()
        
