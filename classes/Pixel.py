import machine
from neopixel import NeoPixel


def initialize_pixel(pin, leds: int) -> NeoPixel:
    pixel = NeoPixel(machine.Pin(pin, machine.Pin.OUT), leds, bpp=3, timing=1)

    return pixel


def clear_segments(segments, from_index: int = 0, to_index: int = 60):
    for s in segments:
        clear_segment(segments[s], from_index, to_index)


def clear_segment(segment: NeoPixel, from_index: int = 0, to_index: int = 60):
    for j in range(from_index, to_index):
        segment[j] = (0, 0, 0)

    segment.write()
