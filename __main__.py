
import pyray as pr

from Services.keyboardservice import KeyboardService
from Services.videoservice import VideoService
from Services.timeservice import TimeService

from Directing.director import Director

from casting.actor import Actor
from casting.actor import Circle
from casting.actor import Rectangle
from casting.actor import TextBased

from casting.cast import Cast


screen_width = 900
screen_height = 600
FPS = 60
CAPTION = "Caption text here"

def main():
    ks = KeyboardService()
    vs = VideoService(screen_width, screen_height, FPS, CAPTION)
    ts = TimeService()

    cast = Cast()

    player1_keys = {
        'a': pr.KEY_A,
        's': pr.KEY_S,
        'd': pr.KEY_D,
        'w': pr.KEY_W
        }
    player1 = TextBased(vs, player1_keys)


    player2_keys = {
        'left': pr.KEY_J,
        'right': pr.KEY_L,
        'down': pr.KEY_K,
        'up': pr.KEY_I
        }
    player2 = TextBased(vs, player2_keys)

    player3_keys = {
        'left': pr.KEY_LEFT,
        'right': pr.KEY_RIGHT,
        'down': pr.KEY_DOWN,
        'up': pr.KEY_RIGHT
        }
    rec_width = 30
    rec_height = 10
    player3 = Rectangle(vs, player3_keys, rec_width, rec_height)

    player4_keys = {
        'left': pr.KEY_T,
        'right': pr.KEY_L,
        'down': pr.KEY_G,
        'up': pr.KEY_H
        }
    circumference = 50
    player4 = Circle(vs, player4_keys, circumference)

   
    cast.add_actor('text_based', player1)
    cast.add_actor('text_based', player2)
    cast.add_actor('rectangles', player3)
    cast.add_actor('circles', player4)



    director = Director(ks, vs, ts, screen_width, screen_height)
    director.run_game(cast)



if __name__ == "__main__":
    main()