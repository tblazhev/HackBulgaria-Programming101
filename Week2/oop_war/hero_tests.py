import unittest
import hero


class HeroTest(unittest.TestCase):
    """Training Academy for the good guys"""
    def setUp(self):
        self.my_hero = hero.Hero("Tedi", 100, "Da Geek")

    def test_init_hero(self):
        self.assertEqual("Tedi", self.my_hero.name)
        self.assertEqual(100, self.my_hero.health)
        self.assertEqual("Da Geek", self.my_hero.nickname)

    def test_known_as(self):
        known_as = self.my_hero.name + " " + self.my_hero.nickname
        self.assertEqual(known_as, self.my_hero.known_as())

if __name__ == '__main__':
    unittest.main()
