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

    # Starts the window and runs program until the window is closed
    def run_game(self, cast):
        self._vs.open_window()

        while self._vs.check_window():
            self.get_inputs(cast)
            self.do_updates(cast)
            self.do_outputs(cast)
        self._vs.close_window()



    def get_inputs(self, cast):
        for actor in cast.get_all_actors():
            self._ks.check_keys_pressed(actor)


    def do_updates(self, cast):
        #changes color every number of seconds
        if self._ts.time_delay(1):
            for actor in cast.get_all_actors():
                # Changes objects location
                #actor._location.random_location(self._vs._width, self._vs._height)
                # Changes objects color  
                actor._color = actor.set_color()

        # Checks for collisions
        for actor in cast.get_all_actors():
            pass

    def do_outputs(self, cast):
        self._vs.clear_buffer()

        for actor in cast.get_all_actors():
            actor.move_actor()
            actor.draw_object(self._vs)

        self._vs.flush_buffer()

