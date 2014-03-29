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

    def test_get_projection_seats(self):
        matrix = self.dbi.get_matrix()
        matrix[1][0] = 1
        matrix[2][4] = 1
        matrix[6][7] = 1
        self.assertEqual(matrix, self.dbi.get_projection_seats(1))

    def test_get_projection_remaining_seats(self):
        self.assertEqual(97, self.dbi.get_projection_remaining_seats(1))

    def test_get_reservation_by_name(self):
        expected = [{
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
        }]
        self.assertEqual(expected, self.dbi.get_reservation_by_name("RadoRado"))

    def test_delete_reservation_by_name(self):
        self.assertTrue(self.dbi.delete_reservation_by_name("RadoRado"))
        self.assertEqual([], self.dbi.get_reservation_by_name("RadoRado"))

    def tearDown(self):
        try:
            os.remove("cinema_test.db")
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
