
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
        'left': pr.KEY_A,
        'right': pr.KEY_D,
        'up': pr.KEY_W,
        'down': pr.KEY_S        
        }
    player1 = TextBased(vs, player1_keys)

    player2_keys = {
        'left': pr.KEY_J,
        'right': pr.KEY_L,
        'up': pr.KEY_I,
        'down': pr.KEY_K
        }
    player2 = TextBased(vs, player2_keys)

    player3_keys = {
        'left': pr.KEY_LEFT,
        'right': pr.KEY_RIGHT,
        'up': pr.KEY_UP,
        'down': pr.KEY_DOWN

        }

    #rec_width = 50
    #rec_height = 30
    #player3 = Rectangle(vs, player3_keys, rec_width, rec_height)
    

    player4_keys = {
        'left': pr.KEY_F,
        'right': pr.KEY_H,
        'up': pr.KEY_T,
        'down': pr.KEY_G
        }
    radius = 50
    player4 = Circle(vs, player4_keys, radius)

    radius = 20
    player3 = Circle(vs, player3_keys, radius)
   
    cast.add_actor('text_based', player1)
    cast.add_actor('text_based', player2)
    cast.add_actor('rectangles', player3)
    cast.add_actor('circles', player4)



    director = Director(ks, vs, ts, screen_width, screen_height)
    director.run_game(cast)



if __name__ == "__main__":
    main()