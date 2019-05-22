from flask import Flask

import views

app = Flask(__name__)


# def create_app():
app.add_url_rule("/", "home_page", view_func=views.home_page)
app.add_url_rule("/movies", "movies_page", view_func=views.movies_page)


# create_app()


if __name__ == '__main__':
    app.run()
