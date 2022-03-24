import pyray as pr

class KeyboardService:

    def check_keys_pressed(self, dict, actor):

        for key in dict:
            if pr.is_key_down(dict[key]):
                actor._move[key] = True
            else: 
                actor._move[key] = False

        
