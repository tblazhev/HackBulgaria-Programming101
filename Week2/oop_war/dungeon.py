from hero import Hero
from fight import Fight


class Dungeon():
    """A dark, scary dungeon"""
    def __init__(self, file_path):
        f = open(file_path, "r")
        map_string = f.read()
        f.close()

        rows = map_string.split("\n")
        self.__map = {}
        count = 0
        for row in rows:
            if row == '':
                continue
            self.__map[count] = list(row)
            count += 1

        self.__players = {}

    def get_map(self):
        return self.__map

    def print_map(self):
        map_string = ""
        for row in self.__map:
            map_string += "".join(self.__map[row]) + "\n"
        print(map_string)

    def get_players(self):
        return self.__players

    def spawn(self, player_name, entity):
        player = {}
        player["object"] = entity
        if type(entity) is Hero:
            char = "H"
        else:
            char = "O"
        player["type"] = char

        found_spawn_point = False
        for row_index in self.__map:
            for col_index, val in enumerate(self.__map[row_index]):
                if val == 'S':
                    self.__map[row_index][col_index] = player["type"]
                    player["position"] = (row_index, col_index)
                    found_spawn_point = True
                    break
            if found_spawn_point:
                break

        if found_spawn_point:
            self.__players[player_name] = player
            return True
        return False

    def get_new_position_from_direction(self, position, direction):
        if direction == "up":
            new_position = (position[0] - 1, position[1])
        elif direction == "down":
            new_position = (position[0] + 1, position[1])
        elif direction == "left":
            new_position = (position[0], position[1] - 1)
        elif direction == "right":
            new_position = (position[0], position[1] + 1)

        if new_position[0] not in self.__map or new_position[1] >= len(self.__map[new_position[0]]):
            return False
        new_position_char = self.__map[new_position[0]][new_position[1]]
        if new_position_char == "#":
            return False
        return new_position

    def initiate_fight(self, player_name, position):
        player_obj = self.__players[player_name]["object"]
        for enemy_player in self.__players:
            if self.__players[enemy_player]["position"] == position:
                new_fight = Fight(player_obj, self.__players[enemy_player]["object"])
                winner = new_fight.simulate_fight()
                if winner == player_obj:
                    loser = enemy_player
                else:
                    loser = player_name
                    player_name = enemy_player
                break
        if loser:
            del self.__players[loser]
        return player_name

    def move(self, player_name, direction):
        position = self.__players[player_name]["position"]
        new_position = self.get_new_position_from_direction(position, direction)
        if not new_position:
            return False

        new_position_char = self.__map[new_position[0]][new_position[1]]

        if new_position_char in ["O", "H"]:
            player_name = self.initiate_fight(player_name, new_position)

        char = self.__players[player_name]["type"]
        self.__map[position[0]][position[1]] = "."
        self.__map[new_position[0]][new_position[1]] = char
        self.__players[player_name]["position"] = new_position

        return True
