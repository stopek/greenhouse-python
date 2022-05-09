import time

from machine import Timer

from classes.Pixel import clear_segments


class Loader:
    current_index = 0
    timer = None
    segments = {}

    def __init__(self, segments):
        self.segments = segments
        self.timer = Timer(0)

    def loop(self, to_index, color=(0, 0, 255)):
        if self.current_index == to_index:
            clear_segments(self.segments)
            self.current_index = 0
        else:
            for s in self.segments:
                segment = self.segments[s]
                segment[self.current_index] = color
                segment.write()

            self.current_index = self.current_index + 1

    def enable(self, to_index: int):
        clear_segments(self.segments)
        self.timer.init(period=50, mode=Timer.PERIODIC, callback=lambda t: self.loop(to_index))

    def disable(self):
        time.sleep(2)
        clear_segments(self.segments)
        self.timer.deinit()
