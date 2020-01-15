import time
import board
import neopixel

pixel_pin = board.D18
num_pixels = 300
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)

def wheel(offset):

    offset = 255 - offset
    if offset < 85:
        return (255 - offset * 3, 0, offset * 3)
    if offset < 170:
        offset -= 85
        return (0, offset * 3, 255 - offset * 3)
    offset -= 170
    return (offset * 3, 255 - offset * 3, 0)


def rainbow_cycle(wait):
    for i in range(num_pixels):
        pixel_index = i * 256 // num_pixels
        pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
    return


def red_cycle(wait):
    for i in range(num_pixels):
        pixel_index = i * 256 // num_pixels
        pixels.fill((0, 0, 0))
        pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
    
    for i in reversed(range(num_pixels)):
        pixel_index = i * 256 // num_pixels
        pixels.fill((0, 0, 0))
        pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
    return
while True:
    # pixels.fill((255, 0, 0)) # Red
    # pixels.show()
    # time.sleep(1)
    # pixels.fill((0, 255, 0)) # Green
    # pixels.show()
    # time.sleep(1)
    # pixels.fill((0, 0, 255)) # Blue
    # pixels.show()
    print("hey")
    time.sleep(1)
    red_cycle(0.000001) 
