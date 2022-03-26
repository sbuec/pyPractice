import pyray as pr

class KeyboardService:

    def check_keys_pressed(self, key_dict, actor):

        for key in key_dict:
            if pr.is_key_down(key_dict[key]):
                actor._move[key] = True
            else: 
                actor._move[key] = False
