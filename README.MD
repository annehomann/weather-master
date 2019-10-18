

# WEATHER MASTER

![](/Users/annehomann/coder_academy/term2/weather_master/w_master.png)



## Flask API Assignment for Coder Academy 

Weather Master is a Flask API that allows you to look up the weather forecast of any city in the world using the OpenWeatherMap API.

both the application and the OpenWeatherMap API and a web browser and the application. The Weather Master presents a web page with an input where a user can type in a city. By clicking on the "Add City" button, the city is added to a database and then a request is made to the OpenWeatherMap API. The API returns the temperature, a brief description of the weather, a weather icon, humidity reading and cloud coverage reading. Using the bootstrap framework, this data is organised into two columns for clean display. 



## Dependencies

- Flask
- Requests
- OS
- Dotenv
- SQLAlchemy
- Flake8



## Pylint vs Flake 8

When running `app.py` through Pylint, you will receive the following errors in your terminal:

```bash
app.py:30:9: E1101: Instance of 'SQLAlchemy' has no 'Column' member (no-member)
app.py:30:19: E1101: Instance of 'SQLAlchemy' has no 'Integer' member (no-member)
app.py:31:11: E1101: Instance of 'SQLAlchemy' has no 'Column' member (no-member)
app.py:31:21: E1101: Instance of 'SQLAlchemy' has no 'String' member (no-member)
app.py:28:0: R0903: Too few public methods (0/2) (too-few-public-methods)
app.py:45:12: E1101: Instance of 'scoped_session' has no 'add' member (no-member)
app.py:46:12: E1101: Instance of 'scoped_session' has no 'commit' member (no-member)
```

This is linked to using SQLAlchemy and is a known problem when using Pylint. 
More about the issue can be read about [here](https://github.com/PyCQA/pylint/issues/1973)

However, when using Flake 8, the errors do not appear. So if you decide to clone/fork this repo to enhance this project further, I recommend you use Flake 8 to check that your code is PEP8 standard 

If you are a hardcore Pylint fan and refuse to use anything else because you loooove getting that sweet score feedback, then you can install a package called `pylint_flask_sqlalchemy` which omits those error messages as if they never existed. The docs are [here](https://pypi.org/project/pylint-flask-sqlalchemy/)



## To Work On Next

The following is what I would like to add for V2.0

- The ability to delete cities from the page so the list doesn't become too long



## License

[![License](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)](http://badges.mit-license.org/)

- **MIT license**

  ©️ Anne Homann 2019