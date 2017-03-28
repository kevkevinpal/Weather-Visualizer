
#to set this up first intsall python on linux machine then type
#pip install apscheduler
import json
import pyowm
import datetime
import time
import mysql.connector

#sets up 
cnx = mysql.connector.connect(user='temperatureUSER', password='!Kms159753', database='tempatureData')
cursor = cnx.cursor()
add_date = ("INSERT INTO Glen_Ellyn"
		"(month, day, year, temp)"
		"VALUES (%s,%s,%s,%s)")


#########################################
#this grabs the current hour
def getTime():
	now = datetime.datetime.now()
	return now.hour
###########################################





#################################################
#this is the Api key and the authenticator
API_key='7286257f9e652145c90b0f1cce93b3e1'
owm = pyowm.OWM(API_key)
##############################################


def setObservationLocation(location):
	###############################################
	#.weather_at_place sets up the location we want to look at
	return owm.weather_at_place(location)
	####################################################

observation = setObservationLocation('Glen Ellyn')

#w is the actual observation itself
w = observation.get_weather()

################################################
#this is loaded in json format
tempInJsonFormat = w.get_temperature('fahrenheit')



def mainRun():
	if time() == 12:
		date = datetime.datetime.now()
		print(getTime())
		

		#this is the info being added to the database
		data_date = (date.month, date.day, date.year, tempInJsonFormat['temp'])
		
		#this is executing the adding to the database
		cursor.execute(add_date,data_date)
		cnx.commit()
		cursor.close()
		cnx.close()

	
		
	else:
		
		print(getTime())
		

while True:
	mainRun()
	time.sleep(3600)





