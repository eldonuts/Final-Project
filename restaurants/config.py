import logging
import os


class BaseConfig(object):
    """Base config class used by all environments and
    inherited by all the other classes below
    """
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    LOGGING_LOCATION = 'restaurants.log'
    LOGGING_LEVEL = logging.DEBUG
    SERVER_PORT = 5000
    SERVER_IP = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///restaurants.db'
    APPLICATION_SETTINGS = 'settings.cfg'
    UPLOAD_FOLDER = 'restaurants/static/restaurant_images'
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
    CLIENT_SECRETS_DIR = 'secrets/'
    SECRET_KEY = 'changeme'


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class ProdConfig(BaseConfig):
    SERVER_PORT = os.getenv('OPENSHIFT_PYTHON_PORT')
    SERVER_IP = os.getenv('OPENSHIFT_PYTHON_IP')
    APPLICATION_SETTINGS = str(os.getenv('OPENSHIFT_DATA_DIR')) + '/settings.cfg'
    LOGGING_LEVEL = logging.WARNING


def configure_app(app):
    """Main config function:
    Works out what environment to configure for based on
    Environment Variable (Dev is assumed if none found),
    then uses that to select the config class, and sets
    logging options.
    :param app: Flask app object
    """

    config = {"Dev": "restaurants.config.DevConfig",
              "Test": "restaurants.config.TestConfig",
              "Prod": "restaurants.config.ProdConfig"
              }

    # Get Environment Variable
    env = os.getenv('RESTAURANT_APP_ENV', 'Dev')

    # Config based on options in this file
    app.config.from_object(config[env])

    # Config based on options in "APPLICATION_SETTINGS" file if it exists (used for anything sensitive)
    try:
        app.config.from_pyfile(app.config.get('APPLICATION_SETTINGS'))
    except IOError:
        print 'could not find ' + app.config.get('APPLICATION_SETTINGS') + ', continuing without it'

    # Logging Config
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(app.config['LOGGING_LOCATION'], maxBytes=1024 * 1024 * 100, backupCount=20)
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
