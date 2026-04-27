==============================================
 Steganography Tool – LSB Image Encoding
 LA2 | Cryptography & Network Security 22CS62
==============================================

SETUP
-----
1. Install Python 3.x (https://python.org)
2. Install dependency:
       pip install Pillow

HOW TO RUN
----------
Step 1 – Generate a sample cover image (first time only):
       python create_sample_image.py

Step 2 – Run the main tool:
       python steganography.py

   Option 1 – Embed:
       Cover image   : cover.png
       Secret message: Hello World!
       Output name   : stego.png

   Option 2 – Extract:
       Stego image   : stego.png
       → Prints the hidden message

IMPORTANT
---------
- Always use PNG format (lossless). JPEG will destroy the hidden data.
- The cover image must be large enough to hold your message.
  A 200x200 PNG can hold up to ~15,000 characters.

FILES
-----
steganography.py        – Main program (embed + extract)
create_sample_image.py  – Generates a test cover image
requirements.txt        – Python dependencies
README.txt              – This file
