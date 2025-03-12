from PIL import Image, ImageDraw
import json
import sys
import os

# from https://stackoverflow.com/questions/15682537
def to_ansi(r, g, b):
  if r == g and g == b:
    if r < 8:
      return 16

    if r > 248:
      return 231

    return round(((r - 8) / 247) * 24) + 232

  ansi = (16
      + (36 * round(r / 255 * 5))
      + (6 * round(g / 255 * 5))
      + round(b / 255 * 5));

  return ansi

width = 95 // 2
height = 27

directory = sys.argv[1]
for idx, file in enumerate(os.listdir(directory)):
  path = directory + '/' + file
  image = Image.open(path).resize((width, height)).convert('RGB').transpose(Image.FLIP_TOP_BOTTOM)

  with open(f'frame-{idx}.gen.conf', 'w') as frame:
    for y in range(height):
      for x in range(width):
        r, g, b = image.getpixel((x, y))
        col = to_ansi(r, g ,b)
        frame.write(f'rename-window -t {y}:={x} {col}\n')
    if idx == 0:
      frame.write('run "sleep 1; tmux source-file \'frame-1.gen.conf\'"')
    else:
      frame.write('run "sleep 1; tmux source-file \'frame-0.gen.conf\'"')

