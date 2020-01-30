from flask import *
import board
import neopixel
import time
import multiprocessing
import psutil






app = Flask(__name__)


pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
counter = 0

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False,
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





@app.route('/rainbow')
def rainbow():
    task_runner('background_two')
    
    return ('', 200)



        
@app.route('/rainbow_single')
def rainbow_single():
    task_runner('background_one')
   
    return ('', 200)


def loop(pattern):
    while True:
        if pattern == 'background_one':
            background_one()
        else:
            background_two()


@app.route('/')
def index():
    return "index"


def task_runner(var):
    processes = psutil.Process().children()
    for p in processes:
        p.kill()
    process = multiprocessing.Process(target=loop, args=(var,))
    process.start()


if __name__ == "__main__":
    app.run(debug=True)

