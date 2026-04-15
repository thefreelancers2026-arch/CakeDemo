import os
from rembg import remove
from PIL import Image

def process_image(filename):
    input_path = os.path.join('assets', filename)
    output_path = os.path.join('assets', filename.replace('.png', '-nobg.png'))
    print(f"Processing {input_path}")
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Failed to process {input_path}: {e}")

images = [
    'nutty_chocolate_cake_1776104211012.png',
    'strawberry_cake_1776104196224.png',
    'vanilla_cake_1776104332418.png',
    'raspberry_cake_1776104471091.png'
]

for img in images:
    process_image(img)
