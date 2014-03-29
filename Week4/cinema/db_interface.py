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

    def get_projection_spots(self, projection_id):
        query = "SELECT spot FROM reservations WHERE projection_id = ?"
        taken_spots = self.dict_cursor.execute(query, (projection_id,)).fetchall()
        spots = self.get_matrix()
        for item in taken_spots:
            spot_tuple = eval(item["spot"])
            spots[spot_tuple[0] - 1][spot_tuple[1] - 1] = 1
        return spots

    def get_matrix(self):
        matrix = [[0 for x in range(10)] for x in range(10)]
        return matrix
