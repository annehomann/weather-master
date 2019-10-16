import requests
from flask import Flask, render_template, request, json, url_for
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
    clothes_data = []

    for city in cities:

        response = requests.get(API_KEY.format(city.name)).json()

        weather = {
            'city' : city.name,
            'temperature' : response['main']['temp'],
            'description' : response ['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
        }

        weather_data.append(weather)

        # temperature = int(weather.get('temperature'))

        # temperature_level = {
        #     0:  "It's scorching hot. Stay cool! Keep hydrated!",
        #     1:  "It's hot and sunny. Don't forget that sunscreen!",
        #     2:  "It's nice and warm today. Time to flex those flip-flops",
        #     3:  "A sweater would be nice in this cool weather",
        #     4:  "It's gonna be cold today. Treat yourself to a hot chocolate!",
        #     5:  "Winter is here! Wear your beanie and gloves!",
        #     6:  "It's Freezing Cold. Maybe don't leave the house."
        # }

        # if temperature >= 35:
        #     return temperature_level[0]
        # elif 27 <= temperature <= 34:
        #     return temperature_level[1]
        # elif 21 <= temperature <= 26:
        #     return temperature_level[2]
        # elif 15 <= temperature <= 20:
        #     return temperature_level[3]
        # elif 4 <= temperature <= 14:
        #     return temperature_level[4]
        # elif -4 <= temperature <= 4:
        #     return temperature_level[5]
        # elif temperature <= -3:
        #     return temperature_level[6]

        # clothes_data.append(temperature_level)

    return render_template('index.html', weather_data=weather_data, clothes_data=clothes_data)


# It is picking up London (first city in list) and displaying option [4]