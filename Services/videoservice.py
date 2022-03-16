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

    # Draws single actor
    def draw_actor(self, cast):
        
        text = cast[0]._text
        font_size = cast[0]._font_size
        color = cast[0]._color
        point_x = cast[0]._location._x
        point_y = cast[0]._location._y
        pr.draw_text(text, point_x, point_y, font_size, color)


    # Draws all actors in specific group
    def draw_actors(self, group):
        pass

    # Draws all actors from all groups
    def draw_all_actors(self, cast):
        cast_length = len(cast)
        for i in range(cast_length):
            text = cast[i]._text
            font_size = cast[i]._font_size
            color = cast[i]._color
            point_x = cast[i]._location._x
            point_y = cast[i]._location._y
            pr.draw_text(text, point_x, point_y, font_size, color)

    # Checks if window is still open
    def check_window(self):
        return not pr.window_should_close()
