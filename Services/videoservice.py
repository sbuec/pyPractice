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

    # Draws single text-based actor
    def draw_text_actor(self, actor):
        
        text = actor._text
        font_size = actor._font_size
        color = actor._color
        point_x = actor._location._x
        point_y = actor._location._y
        pr.draw_text(text, point_x, point_y, font_size, color)

    
    # Draws single rectangle actor
    def draw_rec_actor(self, actor):
        width = actor._x_length
        height = actor._y_length
        color = actor._color
        point_x = actor._location._x
        point_y = actor._location._y
        pr.draw_rectangle(point_x, point_y, width, height, color)


    # Draws single circle actor
    def draw_circ_actor(self, actor):
        radius = actor._radius
        color = actor._color
        point_x = actor._location._x
        point_y = actor._location._y
        pr.draw_circle(point_x, point_y, radius, color)



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
