from machine import Timer

from classes.Builder import build
from classes.Loader import Loader
from classes.Log import Log
from classes.Pixel import initialize_pixel
from classes.Wifi import connect_to_wifi
from config import WIFI_PASSWORD, WIFI_SSID, DATA_ENDPOINT, TOTAL_LEDS, TIMER_PERIOD


def main():
    segments = {
        "green": initialize_pixel(32, TOTAL_LEDS),
        "yellow": initialize_pixel(33, TOTAL_LEDS),
        "black": initialize_pixel(25, TOTAL_LEDS),
        "red": initialize_pixel(26, TOTAL_LEDS)
    }

    Log.empty()
    Log.line()

    loader = Loader(segments)
    loader.enable(10)
    connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)
    loader.disable()

    Log.line()

    build(segments, DATA_ENDPOINT)
    load_timer = Timer(1)
    load_timer.init(period=TIMER_PERIOD, mode=Timer.PERIODIC, callback=lambda t: build(segments, DATA_ENDPOINT))

    Log.empty(2)
    Log.line()


if __name__ == '__main__':
    main()
