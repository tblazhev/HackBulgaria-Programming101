import unittest
import orc
import weapon


class OrcTest(unittest.TestCase):
    """Bootcamp for the bad guys"""
    def setUp(self):
        self.my_orc = orc.Orc("Shrek", 100, 1.6)

    def test_init_orc(self):
        self.assertEqual("Shrek", self.my_orc.name)
        self.assertEqual(100, self.my_orc.health)
        self.assertEqual(1.6, self.my_orc.berserk_factor)

    def test_init_impossibly_angry_orc(self):
        impossibly_angry_orc = orc.Orc("ANGRYYY", 20000, 3)
        self.assertEqual(2, impossibly_angry_orc.berserk_factor)

    def test_init_impossibly_calm_orc(self):
        impossibly_calm_orc = orc.Orc("pussy", 1, -10)
        self.assertEqual(1, impossibly_calm_orc.berserk_factor)

    def test_orc_attack(self):
        my_weapon = weapon.Weapon("Axe", 10, 0.6)
        self.my_orc.equip_weapon(my_weapon)
        damage = self.my_orc.attack()
        self.assertTrue(damage >= 16 and damage <= 32)

if __name__ == '__main__':
    unittest.main()
