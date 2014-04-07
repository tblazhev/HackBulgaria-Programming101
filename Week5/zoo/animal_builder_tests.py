import unittest
from animal_builder import AnimalBuilder
from animal import Animal


class AnimalBuilderTests(unittest.TestCase):
    """docstring for AnimalBuilderTest"""
    def setUp(self):
        self.animal_builder = AnimalBuilder()

    def test_start(self):
        returned = self.animal_builder.start()
        self.assertTrue(returned is self.animal_builder)
        self.assertTrue(isinstance(self.animal_builder.to_build, Animal))

    def test_set_attribute(self):
        returned = self.animal_builder.start().set_attribute("species", "lion")
        self.assertEqual(self.animal_builder.to_build.species, "lion")
        self.assertTrue(returned is self.animal_builder)

    def test_build(self):
        returned = self.animal_builder.start().set_attribute("species", "lion").build()
        self.assertTrue(isinstance(returned, Animal))
        self.assertTrue(self.animal_builder.to_build is None)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
