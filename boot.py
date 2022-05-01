import machine

from classes.Builder import build
from classes.Loader import Loader
from classes.Pixel import initialize_pixel
from classes.Wifi import connect_to_wifi
from config import WIFI_PASSWORD, WIFI_SSID, DATA_ENDPOINT, TOTAL_LEDS

machine.freq(240000000)

def boot():
    print("----------------------------------------------------------------------")
    print()
    print()

    segments = {
        "green": initialize_pixel(32, TOTAL_LEDS),
        "yellow": initialize_pixel(33, TOTAL_LEDS),
        "black": initialize_pixel(25, TOTAL_LEDS),
        "red": initialize_pixel(26, TOTAL_LEDS)
    }

    print("----------------------------------------------------------------------")

    loader = Loader(segments)
    loader.enable(3)
    connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)
    loader.disable()

    print("----------------------------------------------------------------------")

    build(segments, DATA_ENDPOINT)
    loadTimer = machine.Timer(1)
    loadTimer.init(period=5000, mode=machine.Timer.PERIODIC, callback=lambda t: build(segments, DATA_ENDPOINT))

    print()
    print()
    print("----------------------------------------------------------------------")

if __name__ == '__boot__':
    boot()