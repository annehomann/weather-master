#!/usr/bin/python3
'''
Program: Weather Master
Author: Anne Homann
Contact: css011906@coderacademy.edu.au
Date: 2019/10/19
Licence: GPLv3
Version: 0.1

A flask server for accessing and presenting the weather
forecast using the OpenWeatherMap API.
Purpose: To allow a user to find out the weather forecast of a particular city.
'''
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import requests

APP = Flask(__name__)
APP.config['DEBUG'] = True
# The database where cities will be stored
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)


class City(DB.Model):
    ''' Initiates a database to store cities and their weather details '''
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)


@APP.route('/', methods=['GET', 'POST'])
def index():
    ''' Takes the user input, a city, and if it is a new query,
        adds and stores it to the database.  A request is then made
        to the API and the weather details of that city is retrieved and
        displayed back to the user by HTML.'''

    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            new_city_obj = City(name=new_city)
            DB.session.add(new_city_obj)
            DB.session.commit()

    cities = City.query.all()

    # Environment variable, loads hidden API key
    # and stores in api_key variable
    load_dotenv()
    api_key = os.getenv('PROJECT_API_KEY')

    # Empty list for citites and weather to append to
    weather_data = []

    for city in cities:
        # Sends a get request to the OpenWeatherMap API and
        # gets specific weather information
        response = requests.get(api_key.format(city.name)).json()

        # The core of the algorithm!
        weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'humid': response['main']['humidity'],
            'cloudy': response['clouds']['all']
        }

        # Appends each city and its weather information
        # to the waether_data list.
        weather_data.append(weather)

    # Returns weather information onto a HTML page
    return render_template('index.html', weather_data=weather_data)
