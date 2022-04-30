from os import environ

import machine

from classes.Builder import build
from classes.Loader import Loader
from classes.Pixel import initialize_pixel
from classes.Wifi import connect_to_wifi

machine.freq(240000000)

totalLeds = 60

print("----------------------------------------------------------------------")
print()
print()


segments = {
    "green": initialize_pixel(32, totalLeds),
    "yellow": initialize_pixel(33, totalLeds),
    "black": initialize_pixel(25, totalLeds),
    "red": initialize_pixel(26, totalLeds)
}

print("----------------------------------------------------------------------")

loader = Loader(segments)
loader.enable(3)
connect_to_wifi(environ.get('WIFI_SSID'), environ.get('WIFI_PASSWORD'))
loader.disable()

print("----------------------------------------------------------------------")

endpoint = environ.get('DATA_ENDPOINT')
build(segments, endpoint)
loadTimer = machine.Timer(1)
loadTimer.init(period=5000, mode=machine.Timer.PERIODIC, callback=lambda t: build(segments, endpoint))


print()
print()
print("----------------------------------------------------------------------")
