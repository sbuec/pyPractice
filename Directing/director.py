class Director:
    def __init__(self, keyboardservice, videoservice, timeservice, width, height):
        '''
        Creates object and adds video and keyboard services 
        '''
        self._ks = keyboardservice
        self._vs = videoservice
        self._ts = timeservice
        self._width = width
        self._height = height


    def run_game(self, cast):
        self._vs.open_window()

        while self._vs.check_window():
            self.get_inputs(cast)
            self.do_updates(cast)
            self.do_outputs(cast)
        self._vs.close_window()



    def get_inputs(self, cast):
        for actor in cast:
            #Creates True/False list for pressed keys
            actor._move = self._ks.check_keys_pressed(actor._keys).copy()
            actor.move_actor()



    def do_updates(self, cast):
        #changes x/y every number of seconds
        #cast_length = len(cast)
        
        if self._ts.time_delay(1):
            for i in cast:
                # Changes objects location
                #i._location.random_location(self._vs._width, self._vs._height)
            
                # Changes objects color
                i._color = i.set_color()
        



    def do_outputs(self, cast):
        self._vs.clear_buffer()
        
        #self._vs.draw_actor(cast)
        self._vs.draw_all_actors(cast)

        self._vs.flush_buffer()

