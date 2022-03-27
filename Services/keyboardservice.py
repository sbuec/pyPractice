import pyray as pr

class KeyboardService:

    def check_keys_pressed(self, actor):

        for key in actor._keys:
            if pr.is_key_down(actor._keys[key]):
                actor._move[key] = True
            else: 
                actor._move[key] = False
