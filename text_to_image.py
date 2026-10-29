#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
============================================================================
Text to Image Converter

This script converts text into image using the Pillow library.
It supports custom font size and padding size.

Author: Michal Daňhel
Copyright: Copyright (C) 2026 Michal Daňhel
License: GNU GPL v2.0 or later
Version: 1.0

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
============================================================================
"""

__author__ = "Michal Daňhel"
__license__ = "GNU GPL v2.0 or later"
__version__ = "1.0"

import argparse
from PIL import Image, ImageDraw, ImageFont
import os
import sys

def convert_text_to_image(text_file, font_size=18, padding_size=20):
    """
    Converts given text from file into PNG image using the Pillow library.

    Args:
        text_file (str): filename/path to input text file.
        font_size (int): font size in pixels (default is 18).
        padding_size (int): image border padding in pixels (default is 20).
    """

    #
    # Checks if text file exists
    if not os.path.exists(text_file):
        print(f"Error: Input file {text_file} not exists!")
        sys.exit(1)

    # UI
    print(f"Processing file {text_file}")

    #
    # Opens text file and reads its content
    with open(text_file, 'r', encoding="utf-8") as file:
        text_data = file.read()

    #
    # Font settings
    # Info.: Arial font supports Czech characters
    font = ImageFont.truetype(font="arial.ttf", size=font_size, encoding="unic")

    #
    # Getting width and height for final image
    #
    # Creates temporary image just for width and height calculation
    tmp_image = Image.new("RGB", (1,1))
    tmp_image_draw = ImageDraw.Draw(tmp_image)
    bbox = tmp_image_draw.multiline_textbbox((0,0), text_data, font=font)
    #
    image_width = (bbox[2] - bbox[0]) + (padding_size * 2)
    image_height = (bbox[3] - bbox[1]) + (padding_size * 2)

    #
    # Generating final image
    #
    # Creates image with white background
    image = Image.new("RGB", (int(image_width), int(image_height)), color="white")
    image_draw = ImageDraw.Draw(image)
    #
    # Draws text at given position with black color
    image_draw.multiline_text((padding_size, padding_size), text_data, fill="black", font=font)

    # Creates output path for image file
    root, extension = os.path.splitext(text_file)
    image_file = root + ".png"

    #
    # Saves final image to file
    image.save(image_file)

    #
    # UI
    print(f"Finish! Image has been saved to {image_file}")

def main():
    parser = argparse.ArgumentParser(description="Text to Image Converter - converts text into image.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("text_file", type=str, help="filename/path to input text file")
    parser.add_argument("--font_size", type=int, default=18, help="font size in pixels (default is 18)")
    parser.add_argument("--padding_size", type=int, default=20, help="image border padding in pixels (default is 20)")
    args = parser.parse_args()

    convert_text_to_image(args.text_file, args.font_size, args.padding_size)

if __name__ == "__main__":
    main()
