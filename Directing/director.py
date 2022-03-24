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
        for actor in cast._actors:
            #Creates True/False list for pressed keys
            self._ks.check_keys_pressed(actor._keys, actor)
            actor.move_player()


            '''
            
    for key in cast._actors:
        text = cast._actors[key]
        print("Text: ", text)
        '''


    def do_updates(self, cast):
        #changes x/y every number of seconds
        #cast_length = len(cast)
        
        if self._ts.time_delay(1):
            for actor in cast:
                # Changes objects location
                #i._location.random_location(self._vs._width, self._vs._height)
            
                # Changes objects color
                actor._color = actor.set_color()
        



    def do_outputs(self, cast):
        self._vs.clear_buffer()
        
        actors = cast.get_all_actors
        self._vs.get_all_actors(actors)

        self._vs.flush_buffer()

