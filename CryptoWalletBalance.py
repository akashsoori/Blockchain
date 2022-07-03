#!/usr/bin/python3

import time
import json

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Raspberry Pi pin configuration:
RST = None
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Set variables
# replace with your own wallet ID (public key NOT private key)
wallet = "1PXLgcjt2SHtRTCLt1yyoqo69Gv6AocoJA"
balance_url = "https://blockchain.info/q/addressbalance/" + wallet

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as this python script!
# Some nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('BEBAS.ttf', 15)
line1 = 0
line2 = 16
# Create drawing object.
draw = ImageDraw.Draw(image)
