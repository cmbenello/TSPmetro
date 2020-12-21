from metro import *
from WebScraping import *
from node import *
from BingMaps import *
from FileCreator import *
import timeit
wiki_url = 'https://en.wikipedia.org/wiki/List_of_London_Underground_stations'
temp = "https://www.google.co.uk/maps/dir/High+Street+Kensington,+Kensington+Arcade,+Kensington+High+St,+London/Edgware+Road+Station,+London"
#barons court to east putney, acton town to stamford Brook"
file_name = "Tspfile.txt"

London = Metro(wiki_url,"London","UK")
origin = "High Street Kensington, Kensington Arcade, Kensington High St, London".replace(" ", "+")
destination = "Notting Hill Gate, London".replace(" ", "+")


London.Create_File(True)
