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


    for j in range(256):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)
while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
