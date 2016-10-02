import numpy as numpy
import pandas as pd
import json

def createTable():

	#Save result to file
	with open("taxi_availability.json","r") as outfile:

		data = json.loads(outfile.read())

		valueList = data["value"]

		#print valueList[3][u'Latitude']
		#print valueList[0][u'Longitude']
		lat,lng = [],[]
		for location in valueList:
			lat.append(location["Latitude"])
			lng.append(location["Longitude"])
		df = pd.DataFrame([lat,lng]).T
		df.to_csv('output.txt')

if __name__ =="__main__":
	createTable()
