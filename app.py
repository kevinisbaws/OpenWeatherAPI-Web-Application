from flask import Flask, render_template, request
from datetime import datetime
import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHERAPP_API_KEY")


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

  # dictionary to hold the properties of the weather
  weatherInfo = {
    'cityName' : "Enter City Name",
    'zipCode' : "N/A",
    'temperature' : "",
    'humidity' : "",
    'weatherDescription' : "",
    'weatherIcon' : "",
    'timeDisplayed' : ""
  }

  # POST method in order to create new data and post it onto the web application
  if (request.method == "POST"):
    city = request.form.get("city")
    zipCode = request.form.get("zip-code")
    # use the zip code instead of city
    if (not city):
       zipProperties = getZipProperties(zipCode=zipCode)
       cityProperties = getCityProperties(city=zipProperties['name'])
       weatherInfo['zipCode'] = zipProperties['zip']
    # use the city instead of the zip code
    # i need to get the city'd id in order to get the zip code. 
    else:
      cityProperties = getCityProperties(city=city)
      zipProperties = getZipProperties(zipCode=zipCode)

    print(zipCode)
    # Good status codes(200) indicates we need to update the weatherInfo
    if (cityProperties['cod'] == 200):
      weatherInfo['cityName'] = cityProperties['name']
      weatherInfo['temperature'] = f"{cityProperties['main']['temp']}"
      weatherInfo['humidity'] = f"{cityProperties['main']['humidity']}"
      weatherInfo['weatherDescription'] = f"{cityProperties['weather'][0]['description']}"
      icon = cityProperties['weather'][0]['icon']
      weatherInfo['weatherIcon'] = f"http://openweathermap.org/img/wn/{icon}@2x.png"
      currentTime = datetime.now()
      weatherInfo['timeDisplayed'] = currentTime
    # Bad status code(404), instead make the cityName an error message
    else:
      weatherInfo['cityName'] = 'Invalid City Inputted'
    
    response = render_template("index.html", weatherInfo=weatherInfo), 200

    return response
  

  # GET method, meaning we just return an empty index.html file
  else:
    response = render_template("index.html", weatherInfo=weatherInfo)
    return response

  
# getWeatherProperties function: takes in the city as a param, tries to get the json data and return
# the json data
def getCityProperties(city):
  cityURL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

  properties = APICall(cityURL)
  return properties


def getZipProperties(zipCode):
  getZipCode = f"http://api.openweathermap.org/geo/1.0/zip?zip={zipCode}&appid={API_KEY}"
  zipProperties = APICall(getZipCode)

  return zipProperties


def APICall(URL):
  try:
      response = requests.get(URL)
      properties = response.json()
      return properties
  except requests.ConnectionError as CE:
    print(f"Connection error has occurred: {CE}")
  except requests.HTTPError as HE:
    print(f"Bad request has occurred: {HE}")
  except requests.Timeout as TE:
    print(f"Timeout error has occurred: {TE}")
  except requests.RequestException as HE:
    print(f"Bad request has occurred: {HE}")

  return properties


if (__name__ == "__main__"):
  app.run(debug=True)
