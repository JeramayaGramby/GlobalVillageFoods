from flask import Blueprint

auth = Blueprint('auth',__name__)

'''Configuring the login page, logout page and signup page'''

'''Login Page'''
@auth.route('/login')
def login():
    return "<h1>Log in!</h1>"

'''Logout Page'''
@auth.route('/logout')
def logout():
    return "<h1>You have logged out!</h1>"

'''Signup Page'''
@auth.route('/sign-up')
def sign_up():
    return "<h1>Sign Up Now!</h1>"

