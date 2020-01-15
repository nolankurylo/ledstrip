def background_two():
    global break_bool_m
    break_bool_m = True
    print("single")
    global break_bool_s
    while True:
        if break_bool_s:
            break_bool_s = False
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


def background_one():
    global break_bool_s
    break_bool_s = True
    print("hi")
    global break_bool_m
    while True:
        if break_bool_m:
            break_bool_m = False
            break
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
