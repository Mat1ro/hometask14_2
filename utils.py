import sqlite3


def get_movies(name):
    with sqlite3.connect("data/netflix.db") as connection:
        cursor = connection.cursor()
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE title = ?
        ORDER BY release_year desc LIMIT 1
        """
        result = cursor.execute(query, (name,)).fetchall()
        return from_sql_to_json(result)


def year_between_year(from_year, to_year):
    with sqlite3.connect("data/netflix.db") as connection:
        cursor = connection.cursor()
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE release_year BETWEEN ? AND ?
        """
        result = cursor.execute(query, (from_year, to_year,)).fetchall()
        return from_sql_to_json(result)


def children():
    with sqlite3.connect("data/netflix.db") as connection:
        cursor = connection.cursor()
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE rating = 'G'
        """
        result = cursor.execute(query).fetchall()
        return from_sql_to_json(result)


def family():
    with sqlite3.connect("data/netflix.db") as connection:
        cursor = connection.cursor()
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE rating = 'G' OR rating = 'PG' OR rating = 'PG-13'
        """
        result = cursor.execute(query).fetchall()
        return from_sql_to_json(result)


def adult():
    with sqlite3.connect("data/netflix.db") as connection:
        cursor = connection.cursor()
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE rating = 'R' OR rating = 'NC-17'
        """
        result = cursor.execute(query).fetchall()
        return from_sql_to_json(result)


def shows_by_genre(genre):
    with sqlite3.connect("data/netflix.db") as connection:
        cursor = connection.cursor()
        query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        WHERE listed_in LIKE ?
        ORDER BY release_year desc LIMIT 10
        """
        result = cursor.execute(query, (genre,)).fetchall()
        return from_sql_to_json(result)


def from_sql_to_json(data):
    movies = []
    for show in data:
        if len(movies) >= 100:
            break
        movies.append({
            "title": show[0],
            "country": show[1],
            "release_year": show[2],
            "genre": show[3],
            "description": show[4][:-1]
        })
    return movies


print(shows_by_genre('Shows'))
