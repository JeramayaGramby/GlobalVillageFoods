from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

'''Configuring the login page, logout page, signup page, '''

'''Login Page'''
@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html",
        title = 'Login',
        user = 'user',
        boolean = True,
        posts = 'posts')

'''Logout Page'''
@auth.route('/logout')
def logout():
    return render_template("base.html",
        title = 'Logout',
        user = 'user',      
        posts = 'posts')

'''Signup Page'''
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        first_pass_entry = request.form.get('first_pass_entry')
        second_pass_entry = request.form.get('second_pass_entry')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='Error')
        elif len(firstName) < 2:
            flash('Name must be at least two characters', category='Error')
        elif not [first_pass_entry] and len[first_pass_entry] < 8:
            flash('Password must be longer than 8 characters', category='Error')  
        elif first_pass_entry != second_pass_entry:
            flash('Password entries do not match', category='Error')
        else:
            flash('Account successfully created!', category='Success')

    return render_template("sign_up.html",
        title = 'Sign-Up',
        user = 'user',
        posts = 'posts')

'''Admin Page'''
@auth.route('/restricted-access')
def admin():
    return render_template("adminpage.html",
        title = 'Admin_Page',
        user = 'user',
        posts = 'posts')
