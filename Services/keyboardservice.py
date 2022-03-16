import pyray as pr

class KeyboardService:
    def __init__(self):
        self._key_values = []

        self._key_values.append(pr.KEY_A)
        self._key_values.append(pr.KEY_D)
        self._key_values.append(pr.KEY_S)
        self._key_values.append(pr.KEY_W)

        self._key_values.append(pr.KEY_J)
        self._key_values.append(pr.KEY_L)
        self._key_values.append(pr.KEY_K)
        self._key_values.append(pr.KEY_I)

    def is_key_down(self, keys):
        keys_pressed = []

        for key in keys:
            if self._key_values[key]:
                keys_pressed.append[True]
            else: 
                self._keys_pressed[False]

        return keys_pressed




    '''
    def key_query(self, keys):
        keys_pressed = []
        for key in keys:
            if keyispressed(key):
                keys_pressed.append(True)
            else
                keys_pressed.append(False)
        return keys_pressed
    '''