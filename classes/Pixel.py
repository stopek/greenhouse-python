import machine
import neopixel


def initialize_pixel(pin, leds):
    return neopixel.NeoPixel(machine.Pin(pin, machine.Pin.OUT), leds, 3, 1)


def clear_segments(segments, from_index=0, to_index=60):
    for s in segments:
        clear_segment(segments[s], from_index, to_index)


def clear_segment(segment, from_index=0, to_index=60):
    for j in range(from_index, to_index):
        segment[j] = (0, 0, 0)

    segment.write()
