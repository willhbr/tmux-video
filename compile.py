from PIL import Image, ImageDraw
import json
import sys
import os

# from https://stackoverflow.com/questions/15682537
def to_ansi(pixel):
  r, g, b = pixel
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

def compile_images(directory, limit, width, height):
  prev_image = None
  for idx, file in enumerate(sorted(os.listdir(directory))):
    print(f"processing {file}")
    if idx > limit:
      break
    path = directory + '/' + file
    image = Image.open(path).resize((width, height)).convert('RGB').transpose(Image.FLIP_TOP_BOTTOM)

    with open(f'generated/frame-{idx}.gen.conf', 'w') as frame:
      for y in range(height):
        for x in range(width):
          col = to_ansi(image.getpixel((x, y)))
          if prev_image:
            old_col = to_ansi(prev_image.getpixel((x, y)))
            if col == old_col:
              continue
          frame.write(f'renamew -t {y}:={x} {col}\n')
      # frame.write(f'run -d 0.5 -bC "source-file \'generated/frame-{idx + 1}.gen.conf\'"')
    prev_image = image


directory = sys.argv[1]
width = int(sys.argv[2]) // 2 - 1
height = int(sys.argv[3])

print(f"using {width}x{height} = {width * height} windows")

output = 'create-windows.gen.conf'

with open(output, 'w') as f:
  f.write('set-hook -g session-created {\n')
  for _ in range(width):
    f.write('  new-window "exit"\n')
  f.write('  select-window -t :=0\n')
  f.write('}')

print(f"converting images in {directory}...")
compile_images(directory, 200, width, height)
