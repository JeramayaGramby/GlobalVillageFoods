from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

'''Configuring the login page, logout page, signup page, '''

'''Login Page'''
@auth.route('/login')
def login():
    return render_template("login.html",
        title = 'Login',
        user = 'user',
        posts = 'posts')

'''Logout Page'''
@auth.route('/logout')
def logout():
    return render_template("login.html",
        title = 'Login',
        user = 'user',
        posts = 'posts')

'''Signup Page'''
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html",
        title = 'Login',
        user = 'user',
        posts = 'posts')

'''Admin Page'''
@auth.route('/restricted-access')
def admin():
    return render_template("adminpage.html",
        title = 'Admin_Page',
        user = 'user',
        posts = 'posts')
