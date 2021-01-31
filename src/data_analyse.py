import pandas as pd



def data_analyse_menu():
    print("\t\t--Enter--1---Maximum Trend of Language\n")
    print("\t\t--Enter--2---Minimum Trend of Language\n")
    print("\t\t--Enter--3---Exit\n")
    r = int(input("Enter the values:\t\t"))

    if r == 1:
        maxima()

    if r == 2:
        minima()

    if r == 3:
        exit()


def maxima():
    """
    find maximum of the data
    """
    v = pd.read_csv(
        "src\kjpcjs.csv")
    lang = ['Kotlin', 'Java', 'Python', 'C++', 'JavaScript']
    mx = list()
    for i in lang:
        x = max(v[i])
        mx.append(x)

    for i in range(0, 5):
        print(lang[i], "minimum gross is", mx[i])
    data_analyse_menu()    


def minima():
    """
    This is a minima value 
    """
    v = pd.read_csv(
        "src\kjpcjs.csv")
    lang = ['Kotlin', 'Java', 'Python', 'C++', 'JavaScript']
    mx = list()
    for i in lang:
        x = min(v[i])
        mx.append(x)

    for i in range(0, 5):
        print(lang[i], "minimum gross is", mx[i])
    data_analyse_menu()