from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('firstName')
        pass1 = request.form.get('password1')
        pass2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email address is already registered!', category='error')        
        elif len(email) < 4:
            flash('Email should be 4 characters minimum!', category='error')
        elif len (fname) < 2:
            flash('First name should be 8 characters minimum!', category='error')
        elif len(pass1) < 8:
            flash('Password should be 8 characters minimum!', category='error')
        elif pass1 != pass2:
            flash('Passwords do not match!', category='error')
        else:
            new_user = User(email = email, first_name = fname, password = generate_password_hash(pass1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template('sign_up.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged-in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect!', category='error')
        else:
            flash('Email does not exist!', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
