import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('OPENWEATHERAPP_API_KEY')

# getWeatherProperties function: takes in the city as a param, tries to get the json data and return
# the json data

def getWeatherProperties(city):
  cityURL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
  
  try:
    response = requests.get(cityURL)
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
  properties = getWeatherProperties(city="Las Vegas")


