import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.2

while True:
    for i in range(10):
        if cp.switch:
            cp.pixels[i] = (0, 255, 0)
            time.sleep(1)
            cp.pixels[i] = (0, 0, 0)
            time.sleep(1)
        else:
            time.sleep(1)
