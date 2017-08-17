
# to set this up first intsall python on linux machine then type
# pip install apscheduler
import json
import pyowm
import datetime
import time
import csv


locationLookingAt = 'Glen-Ellyn'

API_key = '7286257f9e652145c90b0f1cce93b3e1'
owm = pyowm.OWM(API_key)
observation = owm.weather_at_place(locationLookingAt)
w = observation.get_weather()
tempOfRightNow = w.get_temperature('fahrenheit')
tempatnow = tempOfRightNow['temp']


def writeFile(location, date, temp):
    filename = "Visualizer" + "/" + "data.tsv"
    with open(filename, 'a') as csvfile:
        fieldnames = ['location', 'date', 'temp']
        #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvfile.write(str(date) + "\t" + str(temp) + "\n")
        #writer.writerow({'location': location, 'date': date, 'temp': temp})


def mainRun():
        now = datetime.datetime.now()
        if now.hour == 12:


            date = datetime.date.today()
            todaysday = date.isoformat()
            print(now.hour)
            # this is the info being added to the database
            writeFile(locationLookingAt, date,  tempatnow)
        else:
            print(now.hour)

while True:
    mainRun()
    time.sleep(3600)
