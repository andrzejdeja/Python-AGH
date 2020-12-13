from PIL import Image
from os import listdir
from os.path import splitext
from pathlib import Path

def deleteWords(input, dict):
    for key, val in dict.items():
        input = input.replace(key, val)
    return input
    
dict = {" and ":" or ", " for ":" because ", " why ":" what ", " be ":" was "}

path = Path(__file__).parent.absolute()
for e in listdir(path):
    name, ext = splitext(e)
    try:
        if ext.lower() == ".txt":
            f = open(e, "rt")
            for line in f:
                print(deleteWords(line, dict))
            f.close()
    except OSError:
        print("OSError")

