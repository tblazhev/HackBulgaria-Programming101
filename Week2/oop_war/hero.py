import entity


class Hero(entity.Entity):
    """The good guys"""
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        known_as = self.name + " " + self.nickname
        return known_as
