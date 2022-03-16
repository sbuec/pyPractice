import random

class Color:
    def __init__(self, red = 200, green = 200, blue = 200, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def random_color(self):
        self._red = random.randint(50, 255)
        self._green = random.randint(50, 255)
        self._blue = random.randint(50, 255)

    def random_alpha(self):
        self._alpha = random.randint(50, 255)

    def to_tuple(self):
        return (self._red, self._green, self._blue, self._alpha)   