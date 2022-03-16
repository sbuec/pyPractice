import random

class Location:
    def __init__(self, x = 50, y = 50):
        self._x = x
        self._y = y

    def random_location(self, screen_width, screen_height):
        self._x = random.randint(0, screen_width)
        self._y = random.randint(0, screen_height)