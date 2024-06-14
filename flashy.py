#!/usr/bin/python3

import time
import sys
import board
import neopixel
numPixels = 32
pixels = neopixel.NeoPixel(board.D12, numPixels)

def flash_led(color, times=5, interval=0.5):
    """Flash the given LED a number of times with a specified interval."""
    for _ in range(times):
        for pixel in range(0, len(numPixels)):
            pixels[pixel] = color

    time.sleep(interval)

        for pixel in range(0, len(numPixels)):
            pixels[pixel] = (0, 0, 0)

    time.sleep(interval)

def number_to_color(number):
    """Convert a number between 0 and 254 to an RGB color."""
    if not (0 <= number <= 254):
        raise ValueError("Number must be between 0 and 254")
    # Simple mapping: cycle through colors
    red = (number & 0xE0) >> 5  # Extract red component (3 bits)
    green = (number & 0x1C) >> 2  # Extract green component (3 bits)
    blue = number & 0x03  # Extract blue component (2 bits)

    return (red, green, blue)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != 'flash':
        print("Usage: sudo python3 test.py flash <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[2])
        color = number_to_color(number)
        flash_led(color)
    except ValueError as e:
        print(f"Invalid parameter: {e}")
        sys.exit(1)
