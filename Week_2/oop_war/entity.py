class Entity():
    """And so it begins..."""
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.maxHealth = self.health
        self.weapon = False

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_health(self):
        return self.health

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        self.health += healing_points
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon is not False:
            return True
        return False

    def attack(self):
        if not self.weapon:
            return 0
        coefficient = 1
        if self.weapon.critical_hit():
            coefficient = 2
        return self.weapon.damage * coefficient
