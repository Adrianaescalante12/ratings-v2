"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/movies')
def view_all_movies():
    movies = crud.return_all_movies()
    return render_template('movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """show details on a particular movie"""
    movie_by_id = crud.get_movie_by_id(movie_id)

    ## movie=movie_by_id the left side has to match what you are passing into the jinja template otherwise it won't work
    # and will give you an undefined error

    return render_template('movie_details.html', movie=movie_by_id)


@app.route('/users')
def show_user_email():
    users = crud.return_all_user_emails()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user_info(user_id):
    """show user info"""

    user_by_id = crud.get_all_user_info(user_id)
    return render_template('all_users.html', user=user_by_id)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
