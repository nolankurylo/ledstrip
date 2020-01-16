from flask import *
from concurrent.futures import ThreadPoolExecutor
import board
import neopixel
import time

executor = ThreadPoolExecutor(2)

break_bool1 = False
break_bool2 = False



app = Flask(__name__)


pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)


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
    global break_bool2
    while not break_bool2:
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
    break_bool2 = False
    return


def background_one():
    print("background 1")
    global break_bool1
    while not break_bool1:
        print("in loop 2")
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
    break_bool1 = False
    return





@app.route('/rainbow')
def rainbow():
    reset()
    print("r")
    global executor, break_bool2
    break_bool2 = True
    future = executor.submit(background_one)
    return ('', 200)



        
@app.route('/rainbow_single')
def rainbow_single():
    reset()
    print("rs")
    global executor, break_bool1
    break_bool1 = True
    future = executor.submit(background_two)
    return ('', 200)


def reset():
    pixels.fill((0, 0, 0))
    return




@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    
    app.run(debug=True)
    # threading._start_new_thread(rainbow, ())
    # threading._start_new_thread(rainbow_single, ())
