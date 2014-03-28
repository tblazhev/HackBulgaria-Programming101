import unittest
from movie import Movie


class MovieTest(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("Test Movie", 5)

    def test_create_movie_get_name(self):
        self.assertEqual("Test Movie", self.movie.get_name())


if __name__ == '__main__':
    unittest.main()
