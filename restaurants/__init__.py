from flask import Flask
from restaurants.config import configure_app

# Initialise app object from Flask class
app = Flask(__name__)

# Call config function
configure_app(app)

# Bring in all the views to the app (has to be after app is initialised and configured
from restaurants import views, views_login, views_api, views_menu, views_restaurant
