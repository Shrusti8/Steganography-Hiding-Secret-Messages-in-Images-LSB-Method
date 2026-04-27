# Creates a sample 200x200 colourful PNG to use as a cover image
from PIL import Image
import random

random.seed(42)
img = Image.new('RGB', (200, 200))
pixels = [(random.randint(0,255), random.randint(0,255), random.randint(0,255))
          for _ in range(200*200)]
img.putdata(pixels)
img.save('cover.png')
print('[+] cover.png created (200x200 random colour image)')
