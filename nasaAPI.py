import json
import requests
from datetime import datetime
def main():
	#number of people in space
	response = requests.get("http://api.open-notify.org/astros.json")
	data = response.json()
	print("")
	print("number of people in space" + " " + str(data["number"]))
	print("")
	#longitude and latitude
	print("ISS location below")
	r = requests.get("http://api.open-notify.org/iss-now.json")
	dat1 = r.json()
	print("latitude: " + str(dat1["iss_position"]["latitude"]))
	print("longitude: " + str(dat1["iss_position"]["longitude"]))
	print("")
	
	parameters = {"lat": 40.7128, "lon": 74.0060}
	rq = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)
	dat = rq.json()

	ts = int(dat["response"][0]["risetime"])

	# if you encounter a "year is out of range" error the timestamp
	# may be in milliseconds, try `ts /= 1000` in that case
	print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
	print("duration of pass in minutes  " + str(int(dat["response"][0]["duration"])/60))
	print("")
	



main()