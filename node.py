class Node:
    def __init__(self,Name, ID,Lines): #Name of station, unique id for the station, lines that go through the station
        self.Name = Name
        self.ID = ID
        self.location = 0 #todo calculate with bing maps
        self.Lines = Lines #todo figure out a way to merge with webscraping.py
        self.Connections = 0 #todo do we need this one?