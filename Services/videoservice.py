import pyray as pr

class VideoService:
    def __init__(self, width, height, fps, caption):
        self._width = width
        self._height = height
        self._fps = fps
        self._caption = caption

    # Opens the window
    def open_window(self):
        pr.init_window(self._width, self._height, self._caption)
        pr.set_target_fps(self._fps)

    #Closes the window
    def close_window(self):
        pr.close_window()
    
    # Clears window and prepares it for next frame. 
    # Use at beginning of draw phase
    def clear_buffer(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        
    # Copies buffer to screen
    # Use at end of draw phase
    def flush_buffer(self):
        pr.end_drawing()

    # Checks if window is still open
    def check_window(self):
        return not pr.window_should_close()

    # Draws single actor
    def draw_actor(self, actor):
        
        text = actor[0]._text
        font_size = actor[0]._font_size
        color = actor[0]._color
        point_x = actor[0]._location._x
        point_y = actor[0]._location._y
        pr.draw_text(text, point_x, point_y, font_size, color)


    # Draws all actors in specific group
    def draw_actors(self, group):
        for actor in group:
            self._draw_actor

    # Draws all actors from all groups
    def draw_all_actors(self, cast):
        #cast_length = len(cast)
        for actor in cast:
            text = actor._text
            font_size = actor._font_size
            color = actor._color
            point_x = actor._location._x
            point_y = actor._location._y
            pr.draw_text(text, point_x, point_y, font_size, color)

    # Returns screen height
    def get_height(self):
        return self._height

    # Returns screen width
    def get_width(self):
        return self._width
