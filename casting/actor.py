from General.color import Color
from General.location import Location


class Actor:
    def __init__(self, width, height, keys):
        font_size = 20
        color = self.set_color()
        self._width = width
        self._height = height

        location = Location()
        location.random_location(width, height)

        self._text = ''
        self._font_size = font_size
        self._color = color
        self._location = location

        self._keys = keys
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

    def move_player(self):
        
        #Sets default text to "still"
        #Checks which keys are pressed
        #Changes directions from pressed keys
        for key in self._move:
            if all(value == False for value in self._move.values()):
                self._text = 'still'
            else:
                self._text = ''
            if self._move['left']:
                self._text += 'Left '
                if self._location._x > 0:
                    self._location._x -= 1
            if self._move['right']:
                self._text += 'Right '
                if self._location._x < (self._width - 50):
                    self._location._x += 1
            if self._move['down']:
                self._text += 'Down '
                if self._location._y < (self._height - self._font_size):
                    self._location._y += 1
            if self._move['up']:
                self._text += 'Up'
                if self._location._y > 0:
                    self._location._y -= 1


class TextBased(Actor):
    def __init__(self, width, height, keys):
        super().__init__(width, height, keys)
        '''self._keys = keys
        self._move = {
            'left': False,
            'right': False,
            'down': False,
            'up': False
            }
        '''

class ShapeBased(Actor):
    def __init__(self, width, height, keys):
        super().__init__(width, height, keys)
