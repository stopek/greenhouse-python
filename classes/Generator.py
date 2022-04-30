import math
import time

from classes.Color import hex_to_rgb
from classes.Pixel import clear_segment


def found_next_free(busy, total_leds, ranges):
    for i in range(busy + 1, total_leds):
        if ranges[i] == 1:
            return i

    return -1


def display_segment(segment, np):
    clear_segment(np)

    for part in segment["parts"]:
        lighted = {}
        from_value = part["from"]
        to_value = part["to"]

        real_leds = to_value - from_value
        ranges = [1 for _ in range(real_leds)]

        for color in part["colors"]:
            color_hex = color["color"]
            lighted[color_hex] = 0
            color_rgb = hex_to_rgb(color_hex)
            leds_to_light = math.ceil(color["percentage"] * real_leds / 100)
            nth = math.floor(real_leds / leds_to_light)
            move = math.ceil(math.floor(nth / 2) + (real_leds - leds_to_light * nth) / 2)

            for j in range(real_leds):
                lighted_on = False

                if nth > 0 and (j - move) % nth == 0 and lighted[color_hex] < leds_to_light:
                    if ranges[j] == 1 and j < real_leds:
                        light_on_index = j + from_value
                        np[light_on_index] = color_rgb
                        ranges[j] = 0
                        lighted_on = True
                    else:
                        found = found_next_free(j, real_leds, ranges)
                        if found < 0:
                            found = found_next_free(-1, real_leds, ranges)

                        if found >= 0:
                            light_on_index = found + from_value
                            np[light_on_index] = color_rgb
                            ranges[found] = 0
                            lighted_on = True

                    if lighted_on:
                        lighted[color_hex] = lighted[color_hex] + 1

        np.write()


def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(2)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(10)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
