import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def linegraph():
    """
    Drawing a linegraph
    """
    print("Line Graph Initializing")
    time.sleep(5)
    print("Line Graph Launching")
    a = pd.read_csv("H:\\PROGRAMMING\\PYTHON\\Class 12th Python Project\\csv_data\\kjpcjs.csv")
    a['Week'] = pd.to_datetime(a['Week'])
    data_date = a['Week']
    java_data = a['Java']
    kotlin_data = a['Kotlin']
    c_data = a["C++"]
    p_data = a['Python']
    js_data = a['JavaScript']

# Plotting graph here
    plt.figure(figsize=(10, 5), dpi=150)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.title('Trends Of PROGRAMMING Language', fontdict={'fontweight': 'bold', 'fontsize': 22})
    plt.plot(data_date, java_data, 'r.-', linewidth=2, label="Java")
    plt.plot(data_date, kotlin_data, 'y.-', linewidth=2, label="Kotlin")
    plt.plot(data_date, c_data, 'g.-', linewidth=2, label="C++")
    plt.plot(data_date, p_data, 'b.-', linewidth=2, label="Python")
    plt.plot(data_date, js_data, linewidth=2, label="JavaScript")
    plt.xlabel("DATE")
    plt.ylabel("Percentage of People Learning in INDIA  (%)")
    plt.legend(["Java", "Kotlin", "C++", "Python", "JavaScript"])
    plt.grid(True)
    plt.show()


def splitlinegraph():
    """
    Here we are going to plot seperated line graph.
    """
    print("Split Graph Initalizing")
    time.sleep(3)
    b = pd.read_csv("H:\\PROGRAMMING\\PYTHON\\Class 12th Python Project\\csv_data\\kjpcjs.csv")
    print("Split Line Graph Initialized")
    b['Week'] = pd.to_datetime(b['Week'])
    data_date = b['Week']
    java_data = b['Java']
    kotlin_data = b['Kotlin']
    c_data = b["C++"]
    p_data = b['Python']
    js_data = b['JavaScript']

    plt.subplot(2, 3, 1)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.xlabel("DATE")
    plt.ylabel("%"+"of People")
    plt.plot(data_date, java_data, "g--", label="Java")
    plt.grid(True)
    plt.legend(loc="best")

    plt.subplot(2, 3, 2)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.xlabel("DATE")
    plt.ylabel("%"+"of People")
    plt.plot(data_date, kotlin_data, 'y--', label="Kotlin")
    plt.grid(True)
    plt.legend(loc="best")

    plt.subplot(2, 3, 3)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.xlabel("DATE")
    plt.ylabel("%"+"of People")
    plt.plot(data_date, c_data, color='cyan', label="C++")
    plt.grid(True)
    plt.legend(loc='best')

    plt.subplot(2, 3, 4)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.xlabel("DATE")
    plt.ylabel("%"+"of People")
    plt.plot(data_date, p_data, color='lightblue', linewidth=2, label="Python")
    plt.grid(True)
    plt.legend(loc='best')

    plt.subplot(2, 3, 5)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.plot(data_date, js_data, linewidth=2, label="JavaScript", color='Teal')
    plt.grid(True)
    plt.legend(loc='best')

    plt.subplot(2, 3, 6)
    plt.style.use('seaborn')
    plt.gcf().autofmt_xdate()
    plt.plot(data_date, java_data, 'r.-', linewidth=2, label="Java")
    plt.plot(data_date, kotlin_data, 'y.-', linewidth=2, label="Kotlin")
    plt.plot(data_date, c_data, 'g.-', linewidth=2, label="C++")
    plt.plot(data_date, p_data, 'b.-', linewidth=2, label="Python")
    plt.plot(data_date, js_data, linewidth=2, label="JavaScript")
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()


def splitted_piecharts():
    v = pd.read_csv(
        "kjpcjs.csv")

    #  2015

    df1 = v[
        (v['Week'] < '2016-01-01')
    ]
# 2016
    df2 = v[
        (v['Week'] > '2016-01-01') & (v['Week'] < '2017-01-01')
    ]
#  2017
    df3 = v[
        (v['Week'] > '2017-01-01') & (v['Week'] < '2018-01-01')
    ]
# 2018
    df4 = v[
        (v['Week'] > '2018-01-01') & (v['Week'] < '2019-01-01')
    ]
# 2019
    df5 = v[
        (v['Week'] > '2019-01-01') & (v['Week'] < '2020-01-01')
    ]
# 2020
    df6 = v[
        (v['Week'] > '2020-01-01')
    ]

    lang = ['Kotlin', 'Java', 'Python', 'C++', 'JavaScript']

    av1 = list()

    for i in lang:
        x = sum(df1[i])
        l = len(df1[i])
        avges = x/l
        av1.append(avges)

    av2 = list()

    for r in lang:
        x = sum(df2[r])
        l = len(df2[r])
        avges = x/l
        av2.append(avges)

    av3 = list()

    for v in lang:
        x = sum(df2[v])
        l = len(df2[v])
        avges = x/l
        av3.append(avges)

    av4 = list()

    for b in lang:
        x = sum(df2[b])
        l = len(df2[b])
        avges = x/l
        av4.append(avges)

    av5 = list()

    for n in lang:
        x = sum(df2[n])
        l = len(df2[n])
        avges = x/l
        av5.append(avges)

    av6 = list()

    for m in lang:
        x = sum(df2[m])
        l = len(df2[m])
        avges = x/l
        av6.append(avges)

    cl = ['orange', 'red', 'lightblue', 'green', 'yellow']
    plt.subplot(2, 3, 1)
    plt.style.use('seaborn')
    plt.legend(loc='best', fontsize=5)
    plt.pie(av1, labels=lang, autopct='%1.2f%%', colors=cl, startangle=90)
    plt.title("Language Trend 2015")

    plt.subplot(2, 3, 2)
    plt.style.use('seaborn')
    plt.pie(av2, labels=lang, autopct='%1.2f%%', colors=cl, startangle=90)
    plt.legend(loc='best', fontsize=5)
    plt.title("Language Trend 2016")

    plt.subplot(2, 3, 3)
    plt.style.use('seaborn')
    plt.pie(av3, labels=lang, autopct='%1.2f%%', colors=cl, startangle=90)
    plt.legend(loc='best', fontsize=5)
    plt.title("Language Trend 2017")

    plt.subplot(2, 3, 4)
    plt.style.use('seaborn')
    plt.pie(av4, labels=lang, autopct='%1.2f%%', colors=cl, startangle=90)
    plt.legend(loc='best', fontsize=5)
    plt.title("Language Trend 2018")

    plt.subplot(2, 3, 5)
    plt.style.use('seaborn')
    plt.pie(av5, labels=lang, autopct='%1.2f%%', colors=cl, startangle=90)
    plt.legend(loc='best', fontsize=5)
    plt.title("Language Trend 2019")

    plt.subplot(2, 3, 6)
    plt.style.use('seaborn')
    plt.pie(av6, labels=lang, autopct='%1.2f%%', colors=cl, startangle=90)
    plt.legend(loc='best', fontsize=5)
    plt.title("Language Trend 2020")

    plt.show()


def piecharts():
    """
    this is a piechart
    """
    z = pd.read_csv(
        "kjpcjs.csv")
    lang = ['Kotlin', 'Java', 'Python', 'C++', 'JavaScript']
    i = 0
    av = list()
    for i in lang:
        x = sum(z[i])
        l = len(z[i])
        avges = x/l
        av.append(avges)
    cl = ['orange', 'red', 'lightblue', 'green', 'yellow']
    explodes = [0, 0.2, 0, 0, 0.1]
    plt.pie(av, labels=lang, explode=explodes,
            autopct='%1.1f%%', colors=cl, startangle=90)
    plt.legend(loc=3)
    plt.show()


def bargraphs():
    """
    this is a bar graph splitted languages
    """
    v = pd.read_csv(
        "kjpcjs.csv")

    #  2015

    df1 = v[
        (v['Week'] < '2016-01-01')
    ]
# 2016
    df2 = v[
        (v['Week'] > '2016-01-01') & (v['Week'] < '2017-01-01')
    ]
#  2017
    df3 = v[
        (v['Week'] > '2017-01-01') & (v['Week'] < '2018-01-01')
    ]
# 2018
    df4 = v[
        (v['Week'] > '2018-01-01') & (v['Week'] < '2019-01-01')
    ]
# 2019
    df5 = v[
        (v['Week'] > '2019-01-01') & (v['Week'] < '2020-01-01')
    ]
# 2020
    df6 = v[
        (v['Week'] > '2020-01-01')
    ]

    lang = ['Kotlin', 'Java', 'Python', 'C++', 'JavaScript']

    av1 = list()

    for i in lang:
        x = sum(df1[i])
        l = len(df1[i])
        avges = x/l
        av1.append(avges)

    av2 = list()

    for r in lang:
        x = sum(df2[r])
        l = len(df2[r])
        avges = x/l
        av2.append(avges)

    av3 = list()

    for v in lang:
        x = sum(df2[v])
        l = len(df2[v])
        avges = x/l
        av3.append(avges)

    av4 = list()

    for b in lang:
        x = sum(df2[b])
        l = len(df2[b])
        avges = x/l
        av4.append(avges)

    av5 = list()

    for n in lang:
        x = sum(df2[n])
        l = len(df2[n])
        avges = x/l
        av5.append(avges)

    av6 = list()

    for m in lang:
        x = sum(df2[m])
        l = len(df2[m])
        avges = x/l
        av6.append(avges)

    plt.subplot(2, 3, 1)
    plt.bar(lang, av1)

    plt.subplot(2, 3, 2)
    plt.bar(lang, av2)

    plt.subplot(2, 3, 3)
    plt.bar(lang, av3)

    plt.subplot(2, 3, 4)
    plt.bar(lang, av4)

    plt.subplot(2, 3, 5)
    plt.bar(lang, av5)

    plt.subplot(2, 3, 6)
    plt.bar(lang, av6)

    plt.show()


def bargraph():
    c = pd.read_csv(
        "kjpcjs.csv")
    lang = ['Kotlin', 'Java', 'Python', 'C++', 'JavaScript']
    avgs = list()
    for i in lang:
        x = sum(c[i])
        l = int(len(c[i]))
        avges = x/l
        avgs.append(avges)
    plt.bar(lang, avgs)
    plt.show()

def histogram():
    """
    We are creating a histograms
    """
    a = pd.read_csv("kjpcjs.csv")
    