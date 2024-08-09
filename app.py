from flask import Flask, render_template, request
from functions import getWeatherProperties
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHERAPP_API_KEY")

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():

  # dictionary to hold the properties of the weather
  weatherInfo = {
    'cityName' : "Enter City Name",
    'temperature' : "",
    'humidity' : "",
    'weatherDescription' : ""
  }

  # POST method in order to create new data and post it onto the web application
  if (request.method == "POST"):
    city = request.form.get("city")
    weatherData = getWeatherProperties(city=city)

    # Good status codes(200) indicates we need to update the weatherInfo
    if (weatherData['cod'] == 200):
      weatherInfo['cityName'] = weatherData['name']
      weatherInfo['temperature'] = f"{weatherData['main']['temp']}"
      weatherInfo['humidity'] = f"{weatherData['main']['humidity']}"
      weatherInfo['weatherDescription'] = f"{weatherData['weather'][0]['description']}"
    # Bad status code(404), instead make the cityName an error message
    else:
      weatherInfo['cityName'] = 'Invalid City Inputted'
    
    response = render_template("index.html", weatherInfo=weatherInfo), 200

    return response
  

  # GET method, meaning we just return an empty index.html file
  else:
    response = render_template("index.html", weatherInfo=weatherInfo)
    return response

  

if (__name__ == "__main__"):
  app.run(debug=True)




