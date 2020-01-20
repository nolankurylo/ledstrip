from flask import *
import board
import neopixel
import time
import threading 






app = Flask(__name__)


pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False,
                           pixel_order=ORDER)


pattern = "rainbow"

def rainbow_rgb(offset):

    offset = 255 - offset
    if offset < 85:
        return (255 - offset * 3, 0, offset * 3)
    if offset < 170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3)
    offset -= 170
    return (offset * 3, 255 - offset * 3, 0)


def background_two():
    print("background 2")
    print("in loop 2")
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
    return


def background_one():
    print("background 1")
    print("in loop 1")
    pixels.fill((255, 0, 0))  # Red
    pixels.show()
    time.sleep(1)
    pixels.fill((0, 255, 0))  # Green
    pixels.show()
    time.sleep(1)
    pixels.fill((0, 0, 255))  # Blue
    pixels.show()
    time.sleep(1)
    for i in range(num_pixels):
        pixel_index = i * 256 // num_pixels
        pixels[i] = rainbow_rgb(pixel_index & 255)
        pixels.show()
        time.sleep(0.01)
    return



def infloop():
    global pattern
    
    while True:
        if num_pixels == 0;
            prev_pattern = pattern
            while True:
                if pattern != prev_pattern:
                    break
        num_pixels = 300
        pixels.fill((0, 0, 0))  # Blue
        pixels.show()
        
        print("pattern== " + pattern)
        if pattern == "rainbow":
            background_one()
        elif pattern == "rainbow_single":
            background_two()
        time.sleep(0.1)


@app.route('/rainbow')
def rainbow():
    print("r")
    global pattern, num_pixels
    pattern = "rainbow"
    num_pixels = 0
    return ('', 200)



        
@app.route('/rainbow_single')
def rainbow_single():
    print("rs")
    global pattern, num_pixels
    pattern = "rainbow_single"
    num_pixels = 0
    return ('', 200)





@app.route('/')
def index():
    threading.Thread(target=infloop).start()
    return "index"


if __name__ == "__main__":
    app.run(debug=True)

