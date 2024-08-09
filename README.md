# Task: OpenWeatherMap API Web Program Documentation

> Instructions on the setup and how to run the application

## Setup Requirements

**Prerequisites**: A recent version of Python and pip are installed

## OpenWeatherMap API Setup

- Create an OpenWeatherMap account at https://openweathermap.org.
- Create an OpenWeatherMap key at https://home.openweathermap.org/api_keys.
- Save the key for use later on

## Virtual Environment Setup

**NOTE**: Use pip if on Windows and pip3 on Mac or Linux

- Install 'virtualenv' if it's not already installed

```sh
pip install virtualenv
```

- When installed, find the directory that you want the application to be in and run in terminal

```sh
On Windows:
python -m venv <environment name>
On Mac/Linux:
python3 -m venv <environment name>
```

**note** Don't include the <>

- Activate the virtual environment

```sh
  <venv name>\Scripts\activate (On Windows)
  source <venv name>/bin/activate (On Mac/Linux)
```

## .env Setup

- Create a folder named '.env' in order to store your API keys safely

## Installation

- Clone the repository by entering this in the terminal

```sh
git clone https://github.com/kevinisbaws/
```

- Use pip or pip3 to install all the dependencies

```sh
pip install flask
pip install python-dotenv
pip install requests
or you can just:
pip install -r requirements.txt
```

- Place your saved OpenWeatherMap API key in the environment variable or .env file

## Run

To Run you can type in the terminal after activating your virtual environment

```sh
flask run
or
python app.py # To go into debug mode
```
