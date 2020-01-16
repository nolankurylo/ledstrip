import board
import neopixel
import time

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
    while True:
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
    while True:
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
