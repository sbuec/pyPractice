class Director:
    def __init__(self, keyboardservice, videoservice, timeservice):
        '''
        Creates object and adds video and keyboard services 
        '''
        self._ks = keyboardservice
        self._vs = videoservice
        self._ts = timeservice


    def run_game(self, cast):
        self._vs.open_window()

        while self._vs.check_window():
            self.get_inputs(cast)
            self.do_updates(cast)
            self.do_outputs(cast)
        self._vs.close_window()

    def get_inputs(self, cast):
        cast_length = len(cast)

        for i in range(cast_length):
            value = self._ks.check_keys_pressed(cast[i]._keys)

    def do_updates(self, cast):
        #changes x/y every number of seconds
        cast_length = len(cast)
        '''
        if self._ts.time_delay(1):
            for i in range(cast_length):
                # Changes objects location
                cast[i]._location.random_location(self._vs._width, self._vs._height)
            
                # Changes objects color
                cast[i]._color = cast[i].set_color()
        '''



    def do_outputs(self, cast):
        self._vs.clear_buffer()
        
        #self._vs.draw_actor(cast)
        self._vs.draw_all_actors(cast)

        self._vs.flush_buffer()

