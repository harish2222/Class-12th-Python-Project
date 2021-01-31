# Here are python libraries
from xxlimited import Null

import psycopg2 as pc

# Here are defination libraries
from graphs import *



def dbconn(db, usr, pswd):
    dbc = pc.connect(host="localhost", database=db, user=usr, password=pswd)
    return dbc



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
    8.Histograms
    With user_input in it for the sno numbers of the menu\n
    user_input = int(input("Enter the index value of the following choices:"))
    """
    print("|================GRAPHICAL REPRESENTATION===============|")
    print("\n\t\t1.Show DATA In Line Graph\n")
    print("\t\t2.Show DATA in Splitted Line Graph\n")
    print("\t\t3.Show DATA in Bar Graph\n")
    print("\t\t4.Show DATA in Splitted Bar Graphs\n")
    print("\t\t5.Show DATA in Splitted Pie Chart\n")
    print("\t\t6.Show DATA in Pie Chart\n")
    print("\t\t7.Show DATA in Histogram")
    print("\t\t8.Show DATA in Splitted Histogram")
    print("\t\t9.EXIT\n")

    user_input = int(input("Enter the index value of the following choices:"))

    if user_input == 1:  # |here we will plot a line graph|
        linegraph()
        data_visual()

    elif user_input == 2:  # |plotting a scatter graph|
        splitlinegraph()
        data_visual()

    
    elif user_input == 3:  # |plotting a Bar graph|
        bargraph()
        data_visual()

    elif user_input == 4:  # |Splitted Bar graphs|
        bargraphs()
        data_visual()

    elif user_input == 5:  # |Splitted Piecharts|
        splitted_piecharts()
        data_visual()

    elif user_input == 6:  # |Piechart|
        piecharts()
        data_visual()

    elif user_input == 7:
        histogram()
        data_visual()

    elif user_input == 8:
        seperated_hist()
        data_visual()

    elif user_input == 9:
        exit()

    elif user_input == Null:
        print("Invalid request")
        data_visual()

    elif user_input == "":
        print("Invalid request")
        data_visual()

    else:
        exit()
