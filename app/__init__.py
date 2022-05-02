from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

# Initializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):

    app= Flask(__name__)
