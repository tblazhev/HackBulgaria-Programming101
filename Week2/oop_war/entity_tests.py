import unittest
import entity
import weapon


class EntityTest(unittest.TestCase):
    """The big bang theory"""
    def setUp(self):
        self.my_entity = entity.Entity("Apofis", 1000000)

    def test_init_entity(self):
        self.assertEqual("Apofis", self.my_entity.name)
        self.assertEqual(1000000, self.my_entity.health)

    def test_is_alive(self):
        self.assertTrue(self.my_entity.is_alive())

    def test_is_not_alive(self):
        self.my_entity.health = 0
        self.assertTrue(False is self.my_entity.is_alive())

    def test_get_health(self):
        self.assertEqual(1000000, self.my_entity.get_health())

    def test_take_damage(self):
        health = self.my_entity.get_health()
        self.my_entity.take_damage(50)
        self.assertEqual(health - 50, self.my_entity.get_health())

    def test_take_fatal_damage(self):
        self.my_entity.take_damage(self.my_entity.maxHealth)
        self.assertEqual(0, self.my_entity.get_health())

    def test_take_healing(self):
        health = self.my_entity.get_health()
        self.my_entity.take_damage(50)
        self.assertTrue(self.my_entity.take_healing(20))
        health = health - 50 + 20
        self.assertEqual(health, self.my_entity.get_health())

    def test_take_overhealing(self):
        self.my_entity.take_damage(50)
        self.my_entity.take_healing(1000000)
        self.assertEqual(1000000, self.my_entity.get_health())

    def test_heal_dead_entity(self):
        self.my_entity.take_damage(self.my_entity.maxHealth)
        self.assertTrue(False is self.my_entity.take_healing(50))

    def test_equip_weapon(self):
        magic_weapon = weapon.Weapon("magic_weapon", 20, 0.9)
        self.my_entity.equip_weapon(magic_weapon)
        self.assertTrue(magic_weapon == self.my_entity.weapon)

    def test_has_weapon(self):
        self.assertTrue(not self.my_entity.has_weapon())
        magic_weapon = weapon.Weapon("magic_weapon", 100, 0.9)
        self.my_entity.equip_weapon(magic_weapon)
        self.assertTrue(self.my_entity.has_weapon())

    def test_attack(self):
        self.assertEqual(0, self.my_entity.attack())
        magic_weapon = weapon.Weapon("magic_weapon", 100, 0.9)
        self.my_entity.equip_weapon(magic_weapon)
        damage = self.my_entity.attack()
        self.assertTrue(damage >= 100 and damage <= 200)

if __name__ == '__main__':
    unittest.main()
