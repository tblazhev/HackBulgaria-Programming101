import random


class Fight():
    """For SPARTA!!!"""
    def __init__(self, entity1, entity2):
        self.entity1 = entity1
        self.entity2 = entity2

    def first_attacker(self):
        coin = random.randint(0, 100)
        if coin < 50:
            return self.entity1
        else:
            return self.entity2

    def simulate_fight(self):
        attacker = self.first_attacker()
        if attacker == self.entity1:
            defender = self.entity2
        else:
            defender = self.entity1
        while attacker.is_alive() and defender.is_alive():
            attacker_damage = attacker.attack()
            defender.take_damage(attacker_damage)
            print("%s hits %s with %s for %s damage!" %
                 (attacker.name, defender.name, attacker.weapon.type, attacker_damage))
            if not defender.is_alive():
                print("%s is dead! %s has won! %s is a LEGEND!" %
                     (defender.name, attacker.name, attacker.name))
                return attacker
            temp = attacker
            attacker = defender
            defender = temp
