
import pyray as pr

from Services.keyboardservice import KeyboardService
from Services.videoservice import VideoService
from Services.timeservice import TimeService

from Directing.director import Director

from casting.actor import Actor

WIDTH = 900
HEIGHT = 600
FPS = 60
CAPTION = "Caption text here"

def main():
    ks = KeyboardService()
    vs = VideoService(WIDTH, HEIGHT, FPS, CAPTION)
    ts = TimeService()

    cast = []

    player1_keys = {
        'a': pr.KEY_A,
        's': pr.KEY_S,
        'd': pr.KEY_D,
        'w': pr.KEY_W
        }

    player2_keys = {
        'j': pr.KEY_J,
        'k': pr.KEY_K,
        'l': pr.KEY_L,
        'i': pr.KEY_I
        }

    print('Player 1 a-key: ', player1_keys['a'])
    print('Pr key_down A:', pr.KEY_A)

    cast.append(Actor(WIDTH, HEIGHT, player1_keys))
    cast.append(Actor(WIDTH, HEIGHT, player2_keys))


    cast[0]._text = "k"
    cast[1]._text = "o"

    director = Director(ks, vs, ts)
    director.run_game(cast)



if __name__ == "__main__":
    main()