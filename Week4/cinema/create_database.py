import sqlite3


def create_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS movies
                    (id INTEGER PRIMARY KEY, name text, rating real)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS projections
                    (id INTEGER PRIMARY KEY, movie_id INTEGER, type text, `date` text, time text,
                        FOREIGN KEY(movie_id) REFERENCES movies(id))""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS reservations
                    (id INTEGER PRIMARY KEY, username text, projection_id INTEGER, row int, col int,
                        FOREIGN KEY(projection_id) REFERENCES reservations(id))""")


def insert_movie(cursor, item):
    name = item["name"]
    rating = item["rating"]
    data_to_insert = (name, rating)

    query = "INSERT INTO movies VALUES(NULL, ?, ?)"
    cursor.execute(query, data_to_insert)


def insert_projection(cursor, item):
    movie_id = item["movie_id"]
    type = item["type"]
    date = item["date"]
    time = item["time"]
    data_to_insert = (movie_id, type, date, time)
    query = "INSERT INTO projections VALUES(NULL, ?, ?, ?, ?)"
    cursor.execute(query, data_to_insert)


def insert_reservation(cursor, item):
    username = item["username"]
    projection_id = item["projection_id"]
    row = item["row"]
    col = item["col"]
    data_to_insert = (username, projection_id, row, col)

    query = "INSERT INTO reservations VALUES(NULL, ?, ?, ?, ?)"
    cursor.execute(query, data_to_insert)


def create_database(database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    create_tables(cursor)

    movies = movies_data()
    for movie in movies:
        insert_movie(cursor, movie)

    projections = projections_data()
    for projection in projections:
        insert_projection(cursor, projection)

    reservations = reservations_data()
    for reservation in reservations:
        insert_reservation(cursor, reservation)

    connection.commit()
    connection.close()


def movies_data():
    data = [{
        "id": 1,
        "name": "The Hunger Games: Catching Fire",
        "rating": 7.9
    }, {
        "id": 2,
        "name": "Wreck-It Ralph",
        "rating": 7.8
    }, {
        "id": 3,
        "name": "Her",
        "rating": 8.3
    }]
    return data


def projections_data():
    data = [{
        "id": 1,
        "movie_id": 1,
        "type": "3D",
        "date": "2014-04-01",
        "time": "19:10"
    }, {
        "id": 2,
        "movie_id": 1,
        "type": "4DX",
        "date": "2014-04-02",
        "time": "21:00"
    }, {
        "id": 3,
        "movie_id": 1,
        "type": "2D",
        "date": "2014-04-01",
        "time": "19:00"
    }, {
        "id": 4,
        "movie_id": 3,
        "type": "2D",
        "date": "2014-04-05",
        "time": "20:20"
    }, {
        "id": 5,
        "movie_id": 2,
        "type": "3D",
        "date": "2014-04-02",
        "time": "22:00"
    }, {
        "id": 6,
        "movie_id": 2,
        "type": "2D",
        "date": "2014-04-02",
        "time": "19:30"
    }]
    return data


def reservations_data():
    data = [{
        "id": 1,
        "username": "RadoRado",
        "projection_id": 1,
        "row": 2,
        "col": 1
    }, {
        "id": 2,
        "username": "RadoRado",
        "projection_id": 1,
        "row": 3,
        "col": 5
    }, {
        "id": 3,
        "username": "RadoRado",
        "projection_id": 1,
        "row": 7,
        "col": 8
    }, {
        "id": 4,
        "username": "Ivo",
        "projection_id": 3,
        "row": 1,
        "col": 1
    }, {
        "id": 5,
        "username": "Ivo",
        "projection_id": 3,
        "row": 1,
        "col": 2
    }, {
        "id": 6,
        "username": "Mysterious",
        "projection_id": 5,
        "row": 2,
        "col": 3
    }, {
        "id": 7,
        "username": "Mysterious",
        "projection_id": 5,
        "row": 2,
        "col": 4
    }]
    return data


def main():
    create_database("cinema.db")


if __name__ == '__main__':
    main()
