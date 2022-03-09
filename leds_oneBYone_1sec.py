import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)
## auto_write True = every change is immediately written to the strip of pixels
## if you set auto_write=False then you will  have to call pixels.show() when you want to actually write color data out.
## brightness (range from 0 off to 1.0 full brightness)

while True:
    for i in range(10):
        pixels[i] = (0, 255, 0)
        time.sleep(1)
        pixels.show()
        pixels[i] = (0, 0, 0)
        time.sleep(1)
        pixels.show()
    time.sleep(1)
    
