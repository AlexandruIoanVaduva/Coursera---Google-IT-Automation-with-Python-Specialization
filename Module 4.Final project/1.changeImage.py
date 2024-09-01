# first task for the final project
#!/usr/bin/env python3
import glob
import os
from PIL import Image, ImageOps

def to_do(source_path, dest_path):
    with Image.open(source_path) as im:
        if im.mode != "RGB":
          im = im.convert("RGB")
        size = (600,400)
        # change the image type to jpeg
        ImageOps.contain(im, size).save(dest_path, "JPEG")

# variable for all the files in the image folder
paths = glob.glob("supplier-data/images/*.tiff")

# we run the script
for path in paths:
    to_do(path, path[:-4]+"jpeg")
