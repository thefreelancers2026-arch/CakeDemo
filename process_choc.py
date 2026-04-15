import os
import shutil
from rembg import remove
from PIL import Image

downloads_dir = r"c:\Users\SEC\Downloads"
assets_dir = r"c:\Users\SEC\Downloads\newCake\assets"

files_to_process = [
    "choclate cake 1.jpg",
    "choclate cake 2.jpg",
    "dark Choclate 2.jpg",
    "choclate.jpg",
    "choclte.jpg"
]

for filename in files_to_process:
    input_path = os.path.join(downloads_dir, filename)
    if not os.path.exists(input_path):
        print(f"Not found: {input_path}")
        continue
    
    out_name = filename.replace('.jpg', '-nobg.png').replace(' ', '_')
    output_path = os.path.join(assets_dir, out_name)
    
    print(f"Processing {input_path} -> {output_path}")
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Saved: {out_name}")
    except Exception as e:
        print(f"Error: {e}")
