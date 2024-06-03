"""
author: Tarkan Zarrouk
date: 03/18/2024
Hiding information in images
"""

# Imports :D
from PIL import Image


def get_message_from_image(image):
    # TODO read message from image
    w, h = image.size
    pixels = image.load()
    hidden_message_bin = ""

    # Loop over every pixel. Get the "red" component, get the last binary
    # digit, and read it into a variable
    for x in range(w):
        for y in range(h):
            curr = pixels[x, y]
            red = curr[0]
            last_bin = str(red % 2)
            hidden_message_bin += last_bin

    print(hidden_message_bin)
    print(len(hidden_message_bin))

    hidden_message = ""

    for i in range(0, len(hidden_message_bin), 8):
        next_byte = hidden_message_bin[i:i+8]
        next_byte_int = int(next_byte, base=2)
        char = chr(next_byte_int)
        if char == "%":
            break
        
        hidden_message += char

    return hidden_message


def main():
    # Input
    image_filename = "camping.jpg"
    image = Image.open(image_filename)

    # Processing
    hidden_message = get_message_from_image(image)

    # Output
    print(hidden_message)


if __name__ == "__main__":
    main()
