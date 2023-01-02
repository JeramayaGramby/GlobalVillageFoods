'''Make sure to run __init__.py, views.py, auth.py and models.py before executing main.py'''
import os
from flask import Flask
from decouple import config


def create_app():
    ACCESS_KEY = config('ACCESS_KEY')
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ACCESS_KEY'

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
