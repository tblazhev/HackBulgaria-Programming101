import unittest
from db_interface import DBInterface
from subprocess import call
import os

from create_test_database import movies_data, projections_data, reservations_data


class DBInterfaceTest(unittest.TestCase):
    """docstring for DBInterfaceTest"""
    def setUp(self):
        call("py create_test_database.py", shell=True)
        self.dbi = DBInterface("cinema_test.db")
        self.movies = movies_data()
        self.projections = projections_data()
        self.reservations = reservations_data()

    def test_get_movies(self):
        self.movies = sorted(self.movies, key=lambda k: k['rating'], reverse=True)
        self.assertEqual(self.movies, self.dbi.get_movies_by_rating())

    def test_get_movie_projections(self):
        expected = [{
            "id": 1,
            "movie_id": 1,
            "type": "3D",
            "date": "2014-04-01",
            "time": "19:10"
        }, {
            "id": 3,
            "movie_id": 1,
            "type": "2D",
            "date": "2014-04-01",
            "time": "19:00"
        }, {
            "id": 2,
            "movie_id": 1,
            "type": "4DX",
            "date": "2014-04-02",
            "time": "21:00"
        }]
        self.assertEqual(expected, self.dbi.get_movie_projections(1))

    def test_get_movie_projections_for_date(self):
        expected = [{
            "id": 1,
            "movie_id": 1,
            "type": "3D",
            "date": "2014-04-01",
            "time": "19:10"
        }, {
            "id": 3,
            "movie_id": 1,
            "type": "2D",
            "date": "2014-04-01",
            "time": "19:00"
        }]
        self.assertEqual(expected, self.dbi.get_movie_projections(1, "2014-04-01"))

    def test_get_projection_spots(self):
        # matrix = [[0 for x in range(10)] for x in range(10)]
        self.assertEqual(97, len(self.dbi.get_projection_spots(1)))

    def tearDown(self):
        try:
            os.remove("cinema_test.db")
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
