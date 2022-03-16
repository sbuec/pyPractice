import pyray as pr

class TimeService:
    def __init__(self):
        self._past_time = pr.get_time()
        self._current_time = 0.0

    def time_delay(self, wait_time):
        self._current_time = pr.get_time()

        if (self._current_time - self._past_time) > wait_time:
            self._past_time = self._current_time
            return True
        else:
            return False
