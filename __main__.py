
import pyray as pr

from Services.keyboardservice import KeyboardService
from Services.videoservice import VideoService
from Services.timeservice import TimeService

from Directing.director import Director

from casting.actor import Actor

WIDTH = 900
HEIGHT = 600
FPS = 60
CAPTION = 'Caption text here'

def main():
    ks = KeyboardService()
    vs = VideoService(WIDTH, HEIGHT, FPS, CAPTION)
    ts = TimeService()

    cast = []

    player1_keys = {
        'left': pr.KEY_A,
        'right': pr.KEY_D,
        'down': pr.KEY_S,
        'up': pr.KEY_W
        }

    player2_keys = {
        'left': pr.KEY_J,
        'right': pr.KEY_L,
        'down': pr.KEY_K,
        'up': pr.KEY_I
        }
    player3_keys = {
        'left': pr.KEY_LEFT,
        'right': pr.KEY_RIGHT,
        'down': pr.KEY_DOWN,
        'up': pr.KEY_UP
        }

    cast.append(Actor(WIDTH, HEIGHT, player1_keys))
    cast.append(Actor(WIDTH, HEIGHT, player2_keys))
    cast.append(Actor(WIDTH, HEIGHT, player3_keys))

    cast[0]._text = 'k'
    cast[1]._text = 'o'
    cast[2]._text = 'T'


    director = Director(ks, vs, ts, WIDTH, HEIGHT)
    director.run_game(cast)



if __name__ == "__main__":
    main()