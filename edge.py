class Edge:
    def __init__(self, Weight, Instructions): #Edge id, weight of the edge, instructions to take if you use the edge
        self.Weight = Weight
        self.Instructions = Instructions #instructions is a dictionary split into instructions + polylines

import requests

def links():
    '''https: // commons.wikimedia.org / wiki / London_Underground_geographic_maps / CSV contains information about lines may have to use
    https://www.whatdotheyknow.com/request/512947/response/1238210/attach/3/Stations%2020180921.csv.txt?cookie_passthrough=1
    https://towardsdatascience.com/what-would-the-london-tube-map-look-like-if-data-scientists-designed-it-cfcc38bf2c76
    maybe good for drawing https://www.yworks.com/products/yfiles
    https://www.interline.io/docs/here-xyz/tutorials/tutorial-2/#7
    https://www.interline.io/docs/here-xyz/tutorials/tutorial-2/#7
    transitland api key = Here's your link: http://url3189.interline.io/ls/click?upn=PH8hGLEhXS962PdwXcN5VRE9NrSx-2F1nfpGSWTH7YupX6jktbw-2FgVClft0MdA2U6iXVON5p-2B29xX8wPKEPCJjLrJ4CtWjtMsa7LJ-2BZDTGvVTZmAzyjOCJ3z57xSjvGvKiUEjb_9BUcJuAv9-2B4n22zd4KeXkGhhRAJxtHXIcEmu-2Ba2rrXjuGusFJKZZojQsSxHjcinmsB-2FR0Ix4x0hF-2BllhKPKAF44IRDtdNbexsZvGJSLo6WWi0ajp8fJQb0knG64ahsi3WF2VmE-2FqJGkZoAp9IlGRHZfMrj4V50XZQj5D-2BCs1mro-2FT-2B2fMllh0CmBc2p-2BqHJnrfWNpQFf4dAl0BdjHl03Zfes-2BifxSKThM-2BcDdYnyC0Q-3D
    easiest solution could be to read the map, maybe would be easier to draw connections this way
    https://developers.arcgis.com/python/guide/performing-route-analyses/
    maybe draw in polylines google maps
    https://towardsdatascience.com/i-built-the-t-with-python-and-revamped-it-632127364f4e
    '''