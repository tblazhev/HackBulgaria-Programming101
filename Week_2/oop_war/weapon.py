import random


class Weapon():
    """OUCH!"""
    def __init__(self, type, damage, critical_strike_percent):
        if critical_strike_percent > 1:
            critical_strike_percent = 1
        elif critical_strike_percent < 0:
            critical_strike_percent = 0

        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        num = random.random()
        if num <= self.critical_strike_percent:
            return True
        return False
