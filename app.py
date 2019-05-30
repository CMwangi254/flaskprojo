from flask import Flask

import views
from database import Database

app = Flask(__name__)


# def create_app():
app.add_url_rule("/", "home_page", view_func=views.home_page)
app.add_url_rule("/movies", "movies_page", view_func=views.movies_page, methods=["GET", "POST"])
app.add_url_rule("/movies/<int:movie_key>", "movie_page", view_func=views.movie_page)
app.add_url_rule("/new-movie", "movie_add_page", view_func=views.movie_add_page, methods=["GET", "POST"])
app.add_url_rule("/movies/<int:movie_key>/edit", "movie_edit_page", view_func=views.movie_edit_page, methods=["GET", "POST"])

db = Database()
app.config["db"] = db


# create_app()


if __name__ == '__main__':
    app.run()
