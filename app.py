#!/usr/bin/python3
'''
Program: Weather Master
Author: Anne Homann
Contact: css011906@coderacademy.edu.au
Date: 2019/10/19
Licence: GPLv3
Version: 0.1

A flask server for accessing and presenting the weather forecast using the OpenWeatherMap API.
Purpose: To allow a user to find out the weather forecast of a particular city.
'''
import requests
from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy 
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

''' 
Initiates a database to store cities and their weather details 
'''
class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    
''' WRITE A DOCSTRING ABOUT DATABASE HERE '''

    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()

    '''
    Sends a get request to the OpenWeatherMap API and gets specific weather information
    '''
    load_dotenv()
    API_KEY = os.getenv('PROJECT_API_KEY')

    # Empty list for citites and weather to append to
    weather_data = []

    for city in cities:

        response = requests.get(API_KEY.format(city.name)).json()

        # The core of the algorithm
        weather = {
            'city' : city.name,
            'temperature' : response['main']['temp'],
            'description' : response ['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
            'humid' : response['main']['humidity'],
            'cloudy' : response['clouds']['all']
        }

        # Appends each city and it's weather information to the waether_data list.
        weather_data.append(weather)

    '''
    Returns weather information onto a HTML page
    '''
    return render_template('index.html', weather_data=weather_data)