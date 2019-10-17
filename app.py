import requests
from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy 
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        
        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()

    load_dotenv()
    API_KEY = os.getenv('PROJECT_API_KEY')

    weather_data = []

    for city in cities:

        response = requests.get(API_KEY.format(city.name)).json()

        weather = {
            'city' : city.name,
            'temperature' : response['main']['temp'],
            'description' : response ['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

        weather_data.append(weather)

    return render_template('index.html', weather_data=weather_data)