import time
import board
import neopixel
from flask import Flask

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)


app = Flask(__name__)
break_bool = False

def rainbow_rgb(offset):

    offset = 255 - offset
    if offset < 85:
        return (255 - offset * 3, 0, offset * 3)
    if offset < 170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3)
    offset -= 170
    return (offset * 3, 255 - offset * 3, 0)


@app.route('/rainbow')
def rainbow():
    while True:
        if break_bool:
            break_bool = False
            break
        pixels.fill((255, 0, 0)) # Red
        pixels.show()
        time.sleep(1)
        pixels.fill((0, 255, 0)) # Green
        pixels.show()
        time.sleep(1)
        pixels.fill((0, 0, 255)) # Blue
        pixels.show()
        time.sleep(1)
        red_cycle(0.000001) 
        for i in range(num_pixels):
            pixel_index = i * 256 // num_pixels
            pixels[i] = rainbow_rgb(pixel_index & 255)
            pixels.show()
            time.sleep(0.01)
        
@app.route('/rainbow_single')
def rainbow_single():
    while True:
        if break_bool:
            break_bool = False
            break
        for i in range(num_pixels):
            pixel_index = i * 256 // num_pixels
            pixels.fill((0, 0, 0))
            pixels[i] = rainbow_rgb(pixel_index & 255)
            pixels.show()
            time.sleep(0.01)
        
        for i in reversed(range(num_pixels)):
            pixel_index = i * 256 // num_pixels
            pixels.fill((0, 0, 0))
            pixels[i] = rainbow_rgb(pixel_index & 255)
            pixels.show()
            time.sleep(0.01)

@app.route('/reset')
def reset():
    pass




@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    app.run(debug=True)
