class Movie():
    """docstring for Movie"""
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating
