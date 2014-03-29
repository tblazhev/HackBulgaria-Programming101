import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DBInterface():
    """docstring for DBInterface"""
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.dict_cursor = self.conn.cursor()
        self.dict_cursor.row_factory = dict_factory

    def get_movies_by_rating(self):
        query = "SELECT * FROM movies ORDER BY rating DESC"
        movies = self.dict_cursor.execute(query).fetchall()
        return movies

    def get_movie_projections(self, movie_id, date=False):
        if date is not False:
            query = "SELECT * FROM projections WHERE movie_id = ? AND date = ? ORDER BY date"
            query_data = (movie_id, date)
        else:
            query = "SELECT * FROM projections WHERE movie_id = ? ORDER BY date"
            query_data = (movie_id,)
        projections = self.dict_cursor.execute(query, query_data).fetchall()
        return projections

    def get_projection_seats(self, projection_id):
        query = "SELECT row, col FROM reservations WHERE projection_id = ?"
        taken_seats = self.dict_cursor.execute(query, (projection_id,)).fetchall()
        seats = self.get_matrix()
        for item in taken_seats:
            row = item["row"] - 1
            col = item["col"] - 1
            seats[row][col] = 1
        return seats

    def get_projection_remaining_seats(self, projection_id):
        query = "SELECT 100 - COUNT(*) AS count FROM reservations WHERE projection_id = ?"
        available = self.dict_cursor.execute(query, (projection_id,)).fetchone()
        return available["count"]

    def get_reservation_by_name(self, name):
        query = "SELECT * FROM reservations WHERE username = ?"
        return self.dict_cursor.execute(query, (name,)).fetchall()

    def delete_reservation_by_name(self, name):
        query = "DELETE FROM reservations WHERE username = ?"
        self.dict_cursor.execute(query, (name,))
        self.conn.commit()
        return True

    def get_matrix(self):
        matrix = [[0 for x in range(10)] for x in range(10)]
        return matrix
