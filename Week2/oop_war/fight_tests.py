import unittest
import fight
import orc
import hero
import weapon


class FightTest(unittest.TestCase):
    """Use the source, Luke"""
    def setUp(self):
        self.my_hero = hero.Hero("Tedi", 100, "Da Geek")
        super_laptop = weapon.Weapon("Mind-Control Super-Laptop", 15, 0.3)
        self.my_hero.equip_weapon(super_laptop)

        self.my_orc = orc.Orc("Shrek", 100, 1.6)
        ugly_weapon = weapon.Weapon("Bludgeon", 10, 0.8)
        self.my_orc.equip_weapon(ugly_weapon)

        self.legendary_fight = fight.Fight(self.my_hero, self.my_orc)

    def test_init_fight(self):
        self.assertTrue(self.legendary_fight.entity1 == self.my_hero)
        self.assertTrue(self.legendary_fight.entity2 == self.my_orc)

    def test_first_attacker(self):
        attacker = self.legendary_fight.first_attacker()
        self.assertTrue(attacker == self.my_hero or attacker == self.my_orc)

    def test_simulate_fight(self):
        winner = self.legendary_fight.simulate_fight()
        self.assertTrue(self.my_hero.is_alive() != self.my_orc.is_alive())
        self.assertTrue(type(winner) is hero.Hero or type(winner) is orc.Orc)


if __name__ == '__main__':
    unittest.main()
