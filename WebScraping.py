from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import numpy as np
from node import *
import re
from metro import *
from node import *

def Station_Lines(url): #finds the lines that all stations have
    df = pd.read_html(url)[0]
    output = []
    for station_lines in df['Line(s)[*]']:
        temp_lines = []
        index_lines = []
        j = "a"
        station_lines =  re.sub("\[.\]","",station_lines)
        for i in station_lines:
            if i.isupper() == True and j != " ":
                temp_lines.append([i])
            else:
                temp_lines[-1].append(i)
            j = i
        for line in temp_lines:
            index_lines.append("".join(line))
        output.append(index_lines)

    return(output)

def Lines(Station_Lines): #removes duplicates from station_lines
    list_of_lines = []
    for i in Station_Lines:
        for j in i:
            if j not in list_of_lines:
                list_of_lines.append(j)
    return(list_of_lines)

def Stations(url):  #gets a list of stations
    df = pd.read_html(url)[0]
    station_id = []
    for i in range(len(df['Station'])):
        station_id.append(str(df['Station'][i]) + str(i))
    df['ID'] = station_id
    del df['Line(s)[*]']
    df['Lines'] = Station_Lines(url)
    stations = []
    for i in range(len(df['Station'])):
        stations.append(Node(df['Station'][i],df['ID'][i],df['Lines']))
    return(stations)