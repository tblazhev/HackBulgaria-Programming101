import unittest
from movie import Movie


class MovieTest(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("Test Movie", 5)

    def test_create_movie_get_name_and_rating(self):
        self.assertEqual("Test Movie", self.movie.get_name())
        self.assertEqual(5, self.movie.get_rating())


if __name__ == '__main__':
    unittest.main()
