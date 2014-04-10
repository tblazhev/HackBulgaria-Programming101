from animal import Animal
import sqlite3


class AnimalBuilder():
    def __init__(self):
        self.to_build = None

    def start(self):
        self.to_build = Animal()
        return self

    def set_attribute(self, attr_name, attr_value):
        setattr(self.to_build, attr_name, attr_value)
        return self

    def build(self):
        animal_instance = self.to_build
        self.to_build = None
        return animal_instance
