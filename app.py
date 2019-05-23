from flask import Flask

import views
from database import Database
from movie import Movie

app = Flask(__name__)


# def create_app():
app.add_url_rule("/", "home_page", view_func=views.home_page)
app.add_url_rule("/movies", "movies_page", view_func=views.movies_page)
app.add_url_rule("/movies/<int:movie_key>", "movie_page", view_func=views.movie_page)

db = Database()
db.add_movie(Movie("The SlaughterHouse", year=1972))
db.add_movie(Movie("The Shining"))
app.config["db"] = db


# create_app()


if __name__ == '__main__':
    app.run()
