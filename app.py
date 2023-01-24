from flask import Flask, render_template
from utils import *

app = Flask(__name__, template_folder='templates')


@app.route('/movie/<title>')
def hello_world(title):
    shows = get_movies(title)
    return render_template('movie_by_title.html', title=title, shows=shows)


@app.route('/movie/<int:from_year>/to/<int:to_year>')
def from_to_years(from_year, to_year):
    shows = year_between_year(from_year, to_year)
    return render_template('year_to_year.html', shows=shows)


@app.route('/rating/children')
def rating_children():
    shows = children()
    return render_template('films.html', shows=shows)


@app.route('/rating/family')
def rating_family():
    shows = family()
    return render_template('films.html', shows=shows)


@app.route('/rating/adult')
def rating_adult():
    shows = adult()
    return render_template('films.html', shows=shows)


@app.route('/genre/<genre>')
def genre_page(genre):
    shows = shows_by_genre(genre)
    return render_template('films.html', shows=shows)


if __name__ == '__main__':
    app.run()
