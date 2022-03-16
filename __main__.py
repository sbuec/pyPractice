
import pyray as pr
from General.color import Color
from General.location import Location

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
        'a': 0,
        's': 0,
        'd': 0,
        'w': 0
        }

    cast.append(Actor(WIDTH, HEIGHT))

    cast[0]._text = "k"

    director = Director(ks, vs, ts)
    director.run_game(cast)



if __name__ == "__main__":
    main()