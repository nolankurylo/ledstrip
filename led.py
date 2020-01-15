import time
import threading
import random
import board
import neopixel
import redis
from rq import Queue
from flask import *
from background_jobs import background_one, background_two

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
break_bool_s = False
break_bool_m = False
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)


app = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)


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
    global q
    q.empty()
    job = q.enqueue(background_one)
    return ('', 200)



        
@app.route('/rainbow_single')
def rainbow_single():
    global q
    q.empty()
    job = q.enqueue(background_two)
    return ('', 200)

@app.route('/reset')
def reset():
    pass




@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    
    app.run(debug=True)
    # threading._start_new_thread(rainbow, ())
    # threading._start_new_thread(rainbow_single, ())
