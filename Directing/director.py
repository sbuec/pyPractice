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
        print('window closed')

    def get_inputs(self, cast):
        pass

    def do_updates(self, cast):
        #changes x/y every number of seconds
        if self._ts.time_delay(0.5):
            # Changes objects location
            cast[0]._location.random_location(self._vs._width, self._vs._height)
            
            # Changes objects color
            cast[0]._color = cast[0].set_color()



    def do_outputs(self, cast):
        self._vs.clear_buffer()
        
        self._vs.draw_actor(cast)

        self._vs.flush_buffer()

