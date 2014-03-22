import entity


class Orc(entity.Entity):
    """The bad guys"""
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if berserk_factor > 2:
            berserk_factor = 2
        elif berserk_factor < 1:
            berserk_factor = 1
        self.berserk_factor = berserk_factor

    def attack(self):
        return super().attack() * self.berserk_factor
