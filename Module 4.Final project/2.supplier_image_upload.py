# second task for the final project
#!/usr/bin/env python3
import requests
from PIL import Image
import glob

def to_do(source_path):
    url = "http://localhost/upload/"
    try:
        with open(source_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
    except (OSError, requests.exceptions.RequestException) as e:
        print(f"Error uploading {source_path}: {e}")

# variable for all the files in the image folder
paths = glob.glob("supplier-data/images/*.jpeg")

# we run the script
for path in paths:
    to_do(path)
