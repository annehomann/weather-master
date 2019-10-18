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
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import requests

APP = Flask(__name__)
APP.config['DEBUG'] = True
# The database where cities will be stored
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret key used by Flask to sign cookies
APP.config['SECRET_KEY'] = 'shhhh this is a secret'

DB = SQLAlchemy(APP)


class City(DB.Model):
    ''' Initiates a database called 'City" to store the cities in '''
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), nullable=False)


def open_weather(city):
    ''' This function is to request weather data from the
    OpenWeatherMap API '''
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&appid=79430740a2523990da68bf455740aee5'
    # Environment variable, loads hidden API key
    # and stores in api_key variable
    # load_dotenv()
    # api_key = os.getenv('PROJECT_API_KEY')
    # 
    #response = requests.get(api_key).json()
    response = requests.get(url).json()
    return response


@APP.route('/', methods=['GET'])
def index_get():
    ''' Takes the user input, a city, and if it is a new query,
    adds and stores it to the database.  A request is made to
    the API and the weather details of that city is retrieved and
    displayed back to the user by HTML.'''
    cities = City.query.all()

    # Empty list for weather data and city names to append to
    weather_data = []

    for city in cities:
        # Sends a get request to the OpenWeatherMap API and
        # gets specific weather information
        response = open_weather(city.name)

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


@APP.route('/', methods=['POST'])
def index_post():
    ''' If the user types in a city that has yet to be looked up,
    the API will return the weather details and will be displayed
    to the user. If the city has already been looked up, the user
    will be informed that it has already been added. If the user
    types in jargon or text that is not a city, they will be
    informed to try again and type in a valid city name'''
    error_message = ''
    # Retrieving weather data for a new entered city
    new_city = request.form.get('city')

    if new_city:
        # Will check to see if new city is in the db
        # Retrieves first result if it exists
        existing_city = City.query.filter_by(name=new_city).first()

        # If city doesn't exist, add to db
        if not existing_city:

            new_city_data = open_weather(new_city)
            if new_city_data['cod'] == 200:  # 200 code is a successful request
                new_city_obj = City(name=new_city)

                DB.session.add(new_city_obj)
                DB.session.commit()
            else:
                # This will be displayed if a valid city name is not entered
                error_message = "City does not exist. Please try again."
        else:
            # This will display if the city has already been looked up
            error_message = 'City has already been added!'

    if error_message:
        flash(error_message, 'error')
    else:
        # This will display when a new city has been successfully added
        flash('City added successfully')

    return redirect(url_for('index_get'))
