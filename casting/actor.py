from General.color import Color
from General.location import Location


class Actor:
    def __init__(self, WIDTH, HEIGHT, KEYS):
        font_size = 20
        color = self.set_color()
        self._width = WIDTH
        self._height = HEIGHT

        location = Location()
        location.random_location(WIDTH, HEIGHT, font_size)

        self._text = ''
        self._font_size = font_size
        self._color = color
        self._location = location
        self._keys = KEYS
        self._move = {
            'left': False,
            'right': False,
            'down': False,
            'up': False
            }

    def set_color(self):
            color = Color()
            color.random_color()
            color = color.to_tuple()
            return color

    def move_actor(self):
        
        
        #Checks which keys are pressed
        #Changes directions from pressed keys
        for key in self._move:
            self._text = ''
            if self._move['left']:
                self._text += 'left'
                if self._location._x > 0:
                    self._location._x -= 1
            if self._move['right']:
                self._text += 'right'
                if self._location._x < (self._width - 50):
                    self._location._x += 1
            if self._move['down']:
                self._text += 'down'
                if self._location._y < (self._height - self._font_size):
                    self._location._y += 1
            if self._move['up']:
                self._text += 'up'
                if self._location._y > 0:
                    self._location._y -= 1
            else:
                self._text = 'still'