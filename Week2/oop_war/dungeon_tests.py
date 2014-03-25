import unittest
from dungeon import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon


class DungeonTest(unittest.TestCase):
    """Simulation dungeon"""
    def setUp(self):
        file_path = "basic_dungeon.txt"
        self.my_dungeon = Dungeon(file_path)
        self.dungeon_map = {
            0: list("S.##......"),
            1: list("#.##..###."),
            2: list("#.###.###."),
            3: list("#.....###."),
            4: list("###.#####S")
        }

        self.my_hero = Hero("Tedi", 100, "Da Geek")
        super_laptop = Weapon("Mind-Control Super-Laptop", 20, 0.5)
        self.my_hero.equip_weapon(super_laptop)
        self.my_orc = Orc("Shrek", 100, 2)
        ugly_weapon = Weapon("Bludgeon", 10, 0.5)
        self.my_orc.equip_weapon(ugly_weapon)

    def test_init_dungeon(self):
        self.assertEqual(self.dungeon_map, self.my_dungeon.get_map())

    def test_spawn_hero(self):
        self.assertTrue(self.my_dungeon.spawn("HackTedi", self.my_hero))
        dungeon_map = self.my_dungeon.get_map()
        self.dungeon_map[0][0] = 'H'
        self.assertEqual(self.dungeon_map, dungeon_map)

    def test_spawn_orc(self):
        self.assertTrue(self.my_dungeon.spawn("UglyOrc", self.my_orc))
        dungeon_map = self.my_dungeon.get_map()
        self.dungeon_map[0][0] = 'O'
        self.assertEqual(self.dungeon_map, dungeon_map)

    def test_spawn_hero_and_orc(self):
        self.my_dungeon.spawn("HackTedi", self.my_hero)
        self.my_dungeon.spawn("UglyOrc", self.my_orc)
        dungeon_map = self.my_dungeon.get_map()
        self.dungeon_map[0][0] = 'H'
        self.dungeon_map[4][9] = 'O'
        self.assertEqual(self.dungeon_map, dungeon_map)

    def test_spawn_more_than_available(self):
        self.my_dungeon.spawn("HackTedi", self.my_hero)
        self.my_dungeon.spawn("UglyOrc", self.my_orc)
        self.assertTrue(not self.my_dungeon.spawn("UglyOrc2", self.my_orc))

    def test_move(self):
        self.my_dungeon.spawn("HackTedi", self.my_hero)
        self.my_dungeon.move("HackTedi", "right")
        self.dungeon_map[0][0] = "."
        self.dungeon_map[0][1] = "H"
        dungeon_map = self.my_dungeon.get_map()
        self.assertEqual(self.dungeon_map, dungeon_map)

        players = self.my_dungeon.get_players()
        self.assertEqual(players["HackTedi"]["position"], (0, 1))

    def test_move_into_obstacle(self):
        self.my_dungeon.spawn("HackTedi", self.my_hero)
        self.assertTrue(not self.my_dungeon.move("HackTedi", "down"))
        players = self.my_dungeon.get_players()
        self.assertEqual(players["HackTedi"]["position"], (0, 0))

    def test_move_outside_map(self):
        self.my_dungeon.spawn("HackTedi", self.my_hero)
        self.assertTrue(not self.my_dungeon.move("HackTedi", "up"))
        players = self.my_dungeon.get_players()
        self.assertEqual(players["HackTedi"]["position"], (0, 0))

    def test_move_into_enemy(self):
        file_path = "basic_dungeon_for_fight.txt"
        self.my_dungeon = Dungeon(file_path)

        self.my_dungeon.spawn("HackTedi", self.my_hero)
        self.my_dungeon.spawn("UglyOrc", self.my_orc)
        self.my_dungeon.move("HackTedi", "right")
        map_string = ""
        dungeon_map = self.my_dungeon.get_map()
        for row in dungeon_map:
            map_string += "".join(dungeon_map[row]) + "\n"
        self.assertTrue(map_string == ".H\n" or map_string == ".O\n")

        players = self.my_dungeon.get_players()
        self.assertEqual(1, len(players))


if __name__ == '__main__':
    unittest.main()
