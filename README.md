## Udacity FSND Project 3 - Restaurants

#### Summary

This is a simple catalogue app created using Flask, and was created as part of the Udacity Full Stack Nanodegree program. By default it is set up to handle Restaurants and their matching menu items, but could be adapted to any kind of catalogue. The app has Google and Facebook oauth integration, CSRF protection, seperate views for authenticated users, and a JSON/XML API.

#### Requirements

* [Flask](http://flask.pocoo.org/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
* [Flask_WTF](https://flask-wtf.readthedocs.org)
* [WTForms](https://wtforms.readthedocs.org)
* [dicttoxml](https://pypi.python.org/pypi/dicttoxml)
* [oauth2client](https://pypi.python.org/pypi/oauth2client)
* [Werkzeug](http://werkzeug.pocoo.org/)
* [Requests](http://docs.python-requests.org/)

#### Setup

1. Clone to your local machine: ```git clone https://github.com/eldonuts/Udacity-FSND-P3-Restaurants.git```
2. Alter the **config.py** file to your specifications
3. Create a **settings.cfg** file in your /restuarants directory and add a secret key like so (where xxxx is a randomly generated sequence of numbers): ```SECRET_KEY = 'xxxx'```
4. Run: ```python setup.py```
5. To start the app you just need to run: ```python run.py```
6. That's it, you're good to go, if you want some test data please look below.

#### Test Data

If you wish you generate some test data, I have added a script to grab the top 20 restuarants for NYC (from Zomato) and populate them with a bunch of random menu items. If you wish to try this out, just sign up for a Zomato API key [here](https://developers.zomato.com) and add this line to your **settings.cfg** file (where xxxx is your new key): ```ZOMATO_API_KEY = 'xxxx'```.

Once you're ready you can simply run: ```python test_db_populate.py```

#### Credit

* [United](https://bootswatch.com/united/) Bootstrap Theme
