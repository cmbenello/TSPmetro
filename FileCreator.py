#todo how to create a file
import json
from metro import *
from node import *
from WebScraping import *
from edge import *
from BingMaps import coordinates, outliers

def create_dict(metro):
    Stations = {}
    Station_names = []
    lines = sol(metro.Stations)
    coord_dict = outliers(metro)
    for i in metro.Stations:
        #print(str(i.Name)+ " station, "+ str(metro.City_Name))
        Stations[i.ID] = {"Station_Name":str(i.Name), "Lines":str(i.Lines),"Coordinates":coord_dict[i.ID]} #todo figure out conditional formating
        Station_names.append(i.ID)
        print(i.ID)
    Stations_Dict =  {"List of stations": Station_names, "Properties of stations": Stations}

    dict = {"City_Name": metro.City_Name, "Stations":Stations_Dict, "Lines":lines}
    return(dict)

def matrix_grid(connections):
    for columns in range(len(connections)):
        for rows in range(columns):
            print(columns)
            print(rows)
            edge = connections[columns][rows]
            print(edge)
            connections[columns][rows] = [edge.Weight,edge.Instructions]
    return(connections)

def write_file(dict,file_name): #writes to a file
    with open(file_name,'w') as outfile:
        json.dump(dict,outfile,indent=4)

def erase_file(file_name):
    open(file_name,'w').close()

def read_file(file_name): #reads a file
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return(data)