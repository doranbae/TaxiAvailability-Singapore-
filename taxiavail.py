import json
import urllib
from urlparse import urlparse
import httplib2 as http # External library

def main():
	#Authentification parameters
	headers = { 'AccountKey' : 'xxxxxx', 'UniqueUserID': 'xxxxxxxx','accept':'application/json'} #Request results in json

	#API parameters
	uri = 'http://datamall2.mytransport.sg' #Resource URL
	path = '/ltaodataservice/Taxi-Availability'	

	#Build query string & specify type of API call
	target = urlparse(uri + path)
	print target.geturl()
	method = 'GET'
	body = ''

	#Get handel to http
	h = http.Http()

	#Obtain results
	response, content = h.request(
		target.geturl(),
		method,
		body,
		headers)

	#Parse JSON to print
	jsonObj = json.loads(content)
	print json.dumps(jsonObj, sort_keys=True, indent=4)

	#Save result to file
	with open("taxi_availability.json","w") as outfile:
		#Saving jsonObj["d"]
		json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ =="__main__":
	main()

