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


class TextBased(Actor):
    def __init__(self, vs, keys):
        super().__init__(vs, keys)        
        self._text = 'k'
        self._font_size = 20

    def draw_object(self, vs):
        vs.draw_text_actor(self)

    def move_actor(self):
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
            if self._move['up']:
                self._text += 'Up '
                if self._location._y > 0:
                    self._location._y -= 1
            if self._move['down']:
                self._text += 'Down '
                if self._location._y < (self._height - self._font_size):
                    self._location._y += 1


class Rectangle(Actor):
    def __init__(self, vs, keys, p_width, p_height):
        super().__init__(vs, keys)
        self._x_length = p_width
        self._y_length = p_height
        
        self._x0 = location._x
        self._y0 = location._y
        self._x1 = self._x0 + 1
        self._y1 = self._y0 + 1


    def draw_object(self, vs):
        vs.draw_rec_actor(self)
        
    # Move rectangle actor
    def move_actor(self):

        length = self._x_length
        height = self._y_length

        for key in self._move:
            if self._move['left']:
                if self._location._x > 0:
                    self._location._x -= 1
            if self._move['right']:
                if self._location._x < (self._width - length):
                    self._location._x += 1
            if self._move['up']:
                if self._location._y > 0:
                    self._location._y -= 1
            if self._move['down']:
                if self._location._y < (self._height - height):
                    self._location._y += 1


class Circle(Actor):
    def __init__(self, vs, keys, radius):
        super().__init__(vs, keys)
        self._radius = radius

    def draw_object(self, vs):
        vs.draw_circ_actor(self)

        # Moves circle actor
    def move_actor(self):
        for key in self._move:
            if self._move['left']:
                if self._location._x > self._radius:
                    self._location._x -= 1
            if self._move['right']:
                if self._location._x < (self._width - self._radius):
                    self._location._x += 1
            if self._move['up']:
                if self._location._y > self._radius:
                    self._location._y -= 1
            if self._move['down']:
                if self._location._y < (self._height - self._radius):
                    self._location._y += 1



'''
Checks collisions for rectangles

rec1.location._x1 = rec1.location._x0 + self._x_length

rec1
from rec1_x0 to rec1_x1
from rec1_y0 to rec1_y1
if rec1._x0 <= rec2._x0 and rec1._x1 >= rec2._x1:
    if rec1._y0 <= rec2._y1 and rec1._y1 >= rec2._y0:
        STOP MOVEMENT


  x0, y1_________________x1, y1
        |               |
        |    Rec1       |
  x0, y0|_______________|x1, y0
          x0, y1_________________x1, y1
                |               |
                |     Rec2      |
          x0, y0|_______________|x1, y0

circ1
from circ1._x

'''