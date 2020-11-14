from graphs import linegraph
from menu import maincode


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
    print("\n\t\t1.Show DATA In Line Graph")
    print("\t\t2.Show DATA in Scatter Graph")
    print("\t\t3.Show DATA in Dotted Graph")
    print("\t\t4.Show DATA in Bar Graph")
    print("\t\t5.Show DATA in Shape Graph")
    print("\t\t6.Show DATA in Histograph")
    print("\t\t7.Show DATA in Pie Chart")
    print("\t\t8.Back")
    print("\t\t9.")

    user_input = int(input("Enter the index value of the following choices:"))

    if user_input == 1:  # |here we will plot a line graph|
        linegraph()
        data_visual()

    elif user_input == 2:  # |plotting a scatter graph|
        data_visual()

    elif user_input == 3:  # |plotting a dotted graph|
        data_visual()

    elif user_input == 4:  # |plotting a bar graph|
        data_visual()

    elif user_input == 5:  # |shape graphs|
        data_visual()

    elif user_input == 6:  # |histograph |
        data_visual()

    elif user_input == 7:  # |Piechart|
        data_visual()

    elif user_input == 8:
        maincode()

    elif user_input == 9:
        exit()

    elif user_input == "Null":
        print("Invalid request")
        data_visual()

    elif user_input == "":
        print("Invalid request")
        data_visual()

    else:
        print("Invalid options")

        try:
            maincode()
        except Exception as e:
            raise e
