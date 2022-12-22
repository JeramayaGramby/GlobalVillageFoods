from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def home_page():
    return "<h1>Deez Nuts</h1>"