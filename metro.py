from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from WebScraping import *
from WebScraping import Stations, Station_Lines  # always getting unresolved referance
from node import *
from FileCreator import *
from BingMaps import *

class Metro:
    def __init__(self, url,city_name,country_name):  # todo find efficent way of calculating connections
        self.url = url
        self.Country_Name = country_name
        self.City_Name = city_name
        self.Connections = 0
        self.Lines = Station_Lines(url)
        self.Stations = Stations(url)

    def Create_File(self,connections):
        file_name = "Tspfile.txt"
        File_Dict = create_dict(self)
        write_file(File_Dict,file_name)
        if connections == True:
            erase_file(file_name)
            print(type(matrix_grid(connection_matrix(file_name)))) #should create matrix before erasing file9
            File_Dict["Connections"] = matrix_grid(connection_matrix(file_name))
            write_file(File_Dict,file_name)

    def test(self):
        temp = 0
        return(0)
    def Connections(self):  # creates the graph
        temp = 0

    def EndNodes(self):  # create list of endnodes
        temp = 1

    def ShortestPath(self, Start, End):  # finds fastest route between two nodes
        temp = 0

    def CreateComplete(self):  # floyd warshall
        temp = 0
