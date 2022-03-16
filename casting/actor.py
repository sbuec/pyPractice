from General.color import Color
from General.location import Location


class Actor:
    def __init__(self, WIDTH, HEIGHT, KEYS):
        color = self.set_color()

        location = Location()
        location.random_location(WIDTH, HEIGHT)

        self._text = ''
        self._font_size = 20
        self._color = color
        self._location = location
        self._keys = KEYS

    def set_color(self):
        color = Color()
        color.random_color()
        color = color.to_tuple()
        return color