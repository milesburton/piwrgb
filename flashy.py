#!/usr/bin/python3

import time
import sys
import board
import neopixel

numPixels = 32
pixels = neopixel.NeoPixel(board.D12, numPixels)

 fade_leds(start_color, end_color, steps=50, interval=0.002):
    """Fade LEDs from start_color to end_color."""
    for step in range(steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * step / steps
        g = start_color[1] + (end_color[1] - start_color[1]) * step / steps
        b = start_color[2] + (end_color[2] - start_color[2]) * step / steps
        for pixel in range(numPixels):
            pixels[pixel] = (int(r), int(g), int(b))
        pixels.show()
        time.sleep(interval)

def flash_led(startColor, endColor, times=5, fade_steps=50, interval=0.02):
    """Flash the given LED color a number of times with fade in/out."""
    for _ in range(times):
        fade_leds(startColor, endColor, steps=fade_steps, interval=interval)
        time.sleep(interval)
        fade_leds(startColor, endColor, steps=fade_steps, interval=interval)
        time.sleep(interval)
    return color

def number_to_color(number):
    """Convert a number between 0 and 254 to an RGB color."""
    if not (0 <= number <= 254):
        raise ValueError("Number must be between 0 and 254")
    # Simple mapping: cycle through colors
    red = (number & 0xE0) >> 5  # Extract red component (3 bits)
    green = (number & 0x1C) >> 2  # Extract green component (3 bits)
    blue = number & 0x03  # Extract blue component (2 bits)

    return (red * 32, green * 32, blue * 85)  # Scale to 0-255 range

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != 'flash':
        print("Usage: sudo python3 test.py flash <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[2])
        startColor = number_to_color(number)
        flash_led((0,0,0), startColor)
    except ValueError as e:
        print(f"Invalid parameter: {e}")
        sys.exit(1)

