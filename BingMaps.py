import urllib.request
import requests
import polyline
import json
#from googlemaps import GoogleMaps #https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python
from edge import  *
import itertools
from haversine import haversine, Unit
from metro import *
import statistics

MyKey = "AIzaSyDzvRCXujh6NB31Vnf33826Lan75e6gPgs"

origin = "High Street Kensington, Kensington Arcade, Kensington High St, London".replace(" ", "+")
destination = "Notting Hill Gate, London".replace(" ", "+")


def _url(path):
    return ("https://maps.googleapis.com/maps/api/directions/json?{}&mode=transit&key={}".format(path, MyKey))

def route(origin, destination):
    print(_url("origin={}&destination={}&transit_mode=subway".format(origin.replace(" ","+"),destination.replace(" ","+"))))
    #print(_url("origin={}&destination={}&transit_mode=subway".format('High+Street+Kensington,+Kensington+Arcade,+Kensington+High+St,+London', 'Edgware+Road+Station,+London')))
    return (requests.get(_url("origin={}&destination={}&transit_mode=subway".format(origin.replace(" ","+"), destination.replace(" ","+"))))) #this is a key part, becuase it assumes that all underground services use subways instead of trains

def read_file(file_name): #reads a file
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return(data)

x = route(origin,destination).json()
steps = x['routes'][0]['legs'][0]['steps']

def testtfl():
    start = "W85SA"
    destination = "W68AB"

    def _url(path):
        return ("https://api.tfl.gov.uk/" + path)
    def get_stations():
        return requests.get(_url("StopPoint/Type/NaptanMetroStation"))

def testgooglemaps():
    poly_line = 'y}iyHthd@FT\\|@VXN`@j@hBl@nBFNCBPi@CMoG~E]TM?WE}@P{FzAuFxAaD~@}D|@oErAwA\\Q@gADkAIoAUo@[mAu@_@[[_@g@cAg@eBq@cDm@_Dc@}Dc@yHUeGOaFq@oUK_EUkDa@cEe@qDSaAgAyDeDqHiE_JcEsIeG{MiIsQkAgC_@kAEDh@`@BLo@f@[TDTRhBLfB@^OXk@dAIL'
    poly = polyline.decode(poly_line)
    return(poly)

def is_connected_old(origin,destination): #will input origin,destionation but for testing doesn't have
    x = route(origin,destination).json()
    num_routes = 0
    steps = x['routes'][0]['legs'][0]['steps']
    num_steps = 0 #todo find a better way to search through a json file to see the num_stops
    for i in steps: #goes through each of the steps
        if 'transit_details' in i: #if one of the steps is transit
            transit_details = i['transit_details']
            if 'num_stops' in transit_details and 'line' in transit_details: #I'm not sure why they wouldn't be in but I think is better safe
                num_routes +=1
                if transit_details['line']['vehicle']['type'] == "SUBWAY" and transit_details['num_stops'] == 1: #todo find if first validation thing is necessary and the validation about is necessary i think  can all be solved using transit_mode = subway in the link? but then will need a more strict criteria on the station name
                    num_steps += 1 #this is to prevent doing lots of 'stingle' stops
                    #todo check if google maps gives more than one option
    if num_steps == 1 and num_routes == 1:
        return(True)
    else:
        return(False)

def is_connected_old_2(origin,destination):
    x = route(origin, destination).json()
    steps = x['routes'][0]['legs'][0]['steps']
    num_stops = 0  # todo find a better way to search through a json file to see the num_stops
    for i in steps:  # goes through each of the steps
        if 'transit_details' in i:  # if one of the steps is transit
            transit_details = i['transit_details']
            num_stops += transit_details['num_stops']
    if num_stops == 1:
        return (True)
    else:
        return (False)

def is_connected(origin,destination,line):
    x = route(origin, destination).json()
    print(_url("origin={}&destination={}&transit_mode=subway".format(origin, destination)))
    steps = x['routes'][0]['legs'][0]['steps']
    num_stops = 0
    for i in steps:  # goes through each of the steps
        if 'transit_details' in i:  # finds transit step
            transit_details = i['transit_details']
            num_stops += transit_details['num_stops']
            route_time = transit_details["arrival_time"]["value"] - transit_details['departure_time']["value"]
            poly_line = i['polyline']['points']
            Line  = transit_details['line']['name'].replace(" line","")
            instructions = {"Line" : line, "Polyline" : poly_line}
    print(line)
    print(Line)
    if num_stops == 1 and Line == line:
        return (route_time, instructions)
    else:
        return(float('inf'),[])
    #print(steps)
#todo find out how edgware road works
def connection_info(origin,destination):#will input origin,destination but for testing doesn't have
    for i in steps: #goes through each of the steps
        if 'transit_details' in i: #if one of the steps is transit9
            transit_details = i['transit_details']
            route_time = transit_details["arrival_time"]["value"] - transit_details['departure_time']["value"]
            poly_line = i['polyline']['points']
            return(route_time,poly_line)
            # return weight and polyline + maybe instructions? of travel between the two two nodes

def connection_matrix(file_name): #reads file and uses the information to create the adjancency matrix todo figure out how going at different times is going to affect the route commute time? bank holidays? can worry about later in the user input
    file = read_file(file_name)
    city_name = file['City_Name']
    Matrix = []
    temp = []
    Stations_List = file['Stations']['List of stations']
    for i in Stations_List:
        temp.append(float('inf'))
    for i in Stations_List:
        Matrix.append(temp)
    for key,lines in file['Lines'].items():
        print(key)
        print(lines)
        for origin in lines:
            for destination in lines:
                if origin != destination:
                    decoded = file['Stations']['Properties of stations']
                    origin_name = decoded[origin]["Station_Name"] + ", " + str(city_name) #todo neeed to make it unique to the station
                    destination_name = decoded[destination]["Station_Name"] + ", " + str(city_name)
                    row = Stations_List.index(destination)
                    column = Stations_List.index(origin) #todo how does two lines affect the route between stations?
                    time = is_connected(origin_name,destination_name)[0]
                    instructions = is_connected(origin_name,destination_name)[1]
                    Matrix[column][row] = [time,instructions]
                    if time  != float('inf'):
                        print(str(origin_name) + " is connected to " + str(destination_name))
    return(Matrix)

def furthest_on_line(file_name):
    file = read_file(file_name)
    city_name = file['City_Name']
    line_distance = {}
    for key, lines in file['Lines'].items():
        coords_list = []
        for place in lines:
            decoded = file['Stations']['Properties of stations']
            name = decoded[place]["Station_Name"] + ", " + str(city_name)
            coords = decoded[place]["Coordinates"]
            coords_list.append([name,coords])
        line_distance[key] = max_distance(coords_list)
    return(line_distance)

def max_distance(stations):
    max = ['origin','destination',0]
    for origin in stations:
        for destination in stations[stations.index(origin):]:
            if destination[1][0]!= float('inf') and origin[1][0] != float('inf'):
                if distance(origin[1],destination[1]) > max[2]:
                    max[0] = origin
                    max[1] = destination
                    max[2] = distance(origin[1],destination[1])
    return(max)

def test_maps():
    station = 'Chalfont & Latimer'.replace(" ","+")
    #url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + station+ ",+Station+London&componenets=country:GB|locality:London&key="+str(MyKey)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=Winnetka&bounds=34.1,-118.6|34.2,-118.5&key=" + MyKey #to do bounds must be +- 0.1 degrees
    x= requests.get(url).json()
    print(_url("origin={}&destination={}&transit_mode=subway".format('Perivale+station,+London', destination)))
    print(x['results'][0]['geometry']['location']['lat'],x['results'][0]['geometry']['location']['lng'])

def coordinates(place,country): #this is finding the distance between stations so that I search the closest ones on the line - don't think i need though
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&region={}&key={}".format(place.replace(" ", "+"),country, MyKey)
    x = requests.get(url).json()
    return(x['results'][0]['geometry']['location']['lat'],x['results'][0]['geometry']['location']['lng'])

def coordinates_dict(metro):
    coordinates_dict = {}
    for i in metro.Stations:
        print(i.Name)
        coordinates_dict[i.ID] = [coordinates(str(i.Name) + " station, " + str(metro.City_Name), metro.Country_Name),i.Name]
    return(coordinates_dict)

def outliers(metro): #returns a list of coordinates without the outliers
    coord_dict = coordinates_dict(metro)
    x_list = []
    y_list = []
    for key,values in coord_dict.items():
        x_list.append(values[0][0])
        y_list.append(values[0][1])
    mean_x = statistics.mean(x_list)
    mean_y = statistics.mean(y_list)
    sd_x = statistics.stdev(x_list)
    sd_y = statistics.stdev(y_list)
    upper_x = mean_x + 3*sd_x
    lower_x = mean_x - 3*sd_x
    upper_y = mean_y + 3*sd_y
    lower_y = mean_y - 3*sd_y
    output = {}
    problem = {}
    for name, coord in coord_dict.items():
        if (lower_x<coord[0][0]<upper_x) and (lower_y<coord[0][1]<upper_y):
            output[name] = coord
            print(name)
        else:
            problem[name] = coord
    print(output(list(output)[0]))
    known = str(output(list(output)[0]))
    for key,values in problem.items():
        print(known)
        print(problem)
        print(values[1]) #right now trying to figure out how to get coordinates of places that are giving errors

        x = route(str(known) + " station,+" + str(metro.City_Name), str(values[1]) + " station, " + str(metro.City_Name)).json()
        print(x)
    return(output)

def distance(place1,place2):
    if place1[0] != float('inf') and place2[0] != float('inf'):
        return(haversine(place1,place2,unit=Unit.METERS))
#todo nneed to find way to deal with multiple lines between the same nodes - I presume just use the shortest one?

def line_connector(line):
    temp = 0