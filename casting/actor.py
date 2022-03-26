from General.color import Color
from General.location import Location


class Actor:
    def __init__(self, vs, keys):
        color = self.set_color()
        self._width = vs.get_width()
        self._height = vs.get_height()

        location = Location()
        location.random_location(self._width, self._height)

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
    def __init__(self, vs, keys):
        super().__init__(vs, keys)        
        self._text = ''
        self._font_size = 20

class Rectangle(Actor):
    def __init__(self, vs, keys, p_width, p_height):
        super().__init__(vs, keys)
        self._x_length = p_width
        self._y_length = p_height

        
class Circle(Actor):
    def __init__(self, vs, keys, circumference):
        super().__init__(vs, keys)
        self._circumference = circumference
