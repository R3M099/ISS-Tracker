import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts onboard ISS: \n\n")

people = result["people"]

for p in people:
    file.write(p["name"] + " - on board" + "\n")

g = geocoder.ip("me")
file.write("\n Your current lat / long is: " + str(g.latlng))
file.close()

webbrowser.open("iss.txt")

#Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

#Load the world map image
screen.bgpic("map.gif")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
    #Load the current position of the ISS in real time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #Extract the ISS Loaction
    location = result["iss_position"]
    lat = location["latitude"]
    lng = location["longitude"]

    #Output Lat/Lon to the terminal
    lat = float(lat)
    lng = float(lng)

    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lng))

    #Update the ISS Location on the map
    iss.goto(lng, lat)

    #Refresh each 5 seconds
    time.sleep(5)