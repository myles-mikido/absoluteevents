from PIL import Image
import os

folder = "static"
for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        filepath = os.path.join(folder, filename)
        img = Image.open(filepath)
        img.save(filepath, optimize=True, quality=60)
        print(f"Compressed {filename}")