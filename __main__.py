
import pyray as pr

from Services.keyboardservice import KeyboardService
from Services.videoservice import VideoService
from Services.timeservice import TimeService

from Directing.director import Director

from casting.actor import Actor
from casting.actor import Rectangle
from casting.actor import Circle

from casting.cast import Cast


WIDTH = 900
HEIGHT = 600
FPS = 60
CAPTION = 'Caption text here'

def main():
    ks = KeyboardService()
    vs = VideoService(WIDTH, HEIGHT, FPS, CAPTION)
    ts = TimeService()

    cast = Cast()

    # Text-based object
    player1_keys = {
        'left': pr.KEY_A,
        'right': pr.KEY_D,
        'down': pr.KEY_S,
        'up': pr.KEY_W
        }
    player1 = Actor(WIDTH, HEIGHT, player1_keys)

    # Text-based object
    player2_keys = {
        'left': pr.KEY_J,
        'right': pr.KEY_L,
        'down': pr.KEY_K,
        'up': pr.KEY_I
        }
    player2 = Actor(WIDTH, HEIGHT, player2_keys)

    # Shape-based object (rectangle)
    player3_keys = {
        'left': pr.KEY_LEFT,
        'right': pr.KEY_RIGHT,
        'down': pr.KEY_DOWN,
        'up': pr.KEY_RIGHT
        }
    x_length = 30
    y_length = 10
    player3 = Rectangle(WIDTH, HEIGHT, player3_keys, x_length, y_length)

    # Shape-based object (circle)
    player4_keys = {
        'left': pr.KEY_F,
        'right': pr.KEY_H,
        'down': pr.KEY_G,
        'up': pr.KEY_T
        }
    circumference = 30
    player4 = Circle(WIDTH, HEIGHT, player4_keys, circumference)


    cast.add_actor('text_based', player1)
    cast.add_actor('text_based', player2)
    cast.add_actor('shape_based', player3)
    cast.add_actor('shape_based', player4)

    dictionary = {
        'Name1': 50,
        'Name2': 20
        }
    for count in dictionary:
        print('working')

    for count in cast:
        print('working')

    director = Director(ks, vs, ts, WIDTH, HEIGHT)
    director.run_game(cast)



if __name__ == "__main__":
    main()