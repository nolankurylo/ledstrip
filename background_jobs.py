def background_two():
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


def background_one():
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
