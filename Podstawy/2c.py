from PIL import Image
from os import listdir
from os.path import splitext
from pathlib import Path

def convert(path):
    for f in listdir(path):
        name, ext = splitext(f)
        try:
            if ext.lower() in [".jpeg", ".jpg"]:
                image = Image.open(f)
                image.save(name + ".png")
        except OSError:
            print("OSError")
try:
    path = Path(__file__).parent.absolute()
    convert(path)
except OSError:
    print("OSError")

