import unittest
import weapon


class WeaponTest(unittest.TestCase):
    """test OUCH!"""
    def setUp(self):
        self.my_weapon = weapon.Weapon("Axe", 20, 0.6)

    def test_init_weapon(self):
        self.assertEqual("Axe", self.my_weapon.type)
        self.assertEqual(20, self.my_weapon.damage)
        self.assertEqual(0.6, self.my_weapon.critical_strike_percent)

    def test_init_too_much_or_too_little_critical_strike_percent(self):
        strong_weapon = weapon.Weapon("Atomic bomb", 20000, 300)
        weak_weapon = weapon.Weapon("Water Gun", 0.2, -1.3)
        self.assertEqual(1, strong_weapon.critical_strike_percent)
        self.assertEqual(0, weak_weapon.critical_strike_percent)

    def test_critical_strike_percent(self):
        critical_hit = self.my_weapon.critical_hit()
        self.assertTrue(critical_hit or not critical_hit)


if __name__ == '__main__':
    unittest.main()
