import pyray as pr

class KeyboardService:

    def check_keys_pressed(self, keys):
        keys_pressed = []

        keys_length = len(keys)


        for i in range(keys_length):
            if pr.is_key_down(keys[i]):
                keys_pressed.append(True)
            else: 
                keys_pressed.append(False)

        return keys_pressed




    '''
            key_pressed = []
            for i in actor_key_length:
                if pyray.is_key_down(dict)
                    keys_pressed[i] = True
                else:
                    keys_pressed[i] = False
            return keys_pressed
                

            if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

    def key_query(self, keys):
        keys_pressed = []
        for key in keys:
            if keyispressed(key):
                keys_pressed.append(True)
            else
                keys_pressed.append(False)
        return keys_pressed
    '''