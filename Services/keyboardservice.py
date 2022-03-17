import pyray as pr

class KeyboardService:

    def check_keys_pressed(self, dict):
        keys_pressed = dict.copy()

        for key in dict:
            if pr.is_key_down(dict[key]):
                keys_pressed[key] = True
            else: 
                keys_pressed[key] = False
        return keys_pressed
        
