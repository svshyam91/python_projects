"""
This program gives the current weather report using Openweathermap API
To know more about the API used in this program: https://openweathermap.org/current

Author: @svshyam91
Date: 27th May, 2019

"""

import json
import requests

def display_data( weather_details ):
	print("                       _____________WEATHER REPORT_________________")

	print("\n\nTemperature: ",round(weather_details["temperature"],2),"(Celcius)")
	print("Humidity: ",weather_details["humidity"],"%",sep="")
	print("Description:",weather_details["description"])

	# To convert the speed form m/s to km/h, multiply with 3.6
	print("Wind Speed:",float(weather_details["windSpeed"])*3.6,"km/h",sep="")	
	print("\n\n")

def weather_info( data ):
	weather_details={
	"temperature": float(data["main"]["temp"]-273.15),
	"humidity": data["main"]["humidity"],
	"description": data["weather"][0]["description"],
	"windSpeed": data["wind"]["speed"],
	}
	return weather_details

def main():
	# The cities must be from INDIA but it can work for any other country. 
	# Just change the country code in the "api_str"(API URL) variable.
	city=input("Enter the name of the city: ")
	
	# API URL
	api_str="http://api.openweathermap.org/data/2.5/weather?q={},IN\
	&appid=90d4613c85d31a3b2bd4dc4484c62a94".format(city)

	try:
		response=requests.get(api_str)
	except Exception as e:
		print("There is somethings wrong while loading the page..")
		return

	try:
		# Data returned by API
		data=json.loads(response.text)
	except Exception as e:
		print("There is some problem while fetching data from API")
		return

	# print(data)

	# Check the return status of the response
	if int(data["cod"])==404:
		print("Return Status:",data["message"])
	elif int(data["cod"])==200:
		weather_details=weather_info(data)
		display_data(weather_details)

if __name__ == '__main__':
	main()
