from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

from models.models import db, User


def init_auth_routes(app):

    @app.route('/register', methods=['GET', 'POST'])
    def register():

        if request.method == 'POST':

            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            # PostgreSQL integration: use SQLAlchemy ORM queries instead of raw SQL.
            existing_user = User.query.filter(
                (User.email == email) | (User.username == username)
            ).first()

            if existing_user:
                flash('Email or username already exists')
                return redirect(url_for('register'))

            hashed_password = generate_password_hash(password)

            new_user = User(
                username=username,
                email=email,
                password=hashed_password
            )

            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful')
            return redirect(url_for('login'))

        return render_template('register.html')


    @app.route('/login', methods=['GET', 'POST'])
    def login():

        if request.method == 'POST':

            email = request.form.get('email')
            password = request.form.get('password')

            # PostgreSQL integration: authenticate against the users table via SQLAlchemy.
            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):

                login_user(user)

                return redirect(url_for('dashboard'))

            flash('Invalid email or password')

        return render_template('login.html')


    @app.route('/logout')
    @login_required
    def logout():

        logout_user()

        return redirect(url_for('login'))
