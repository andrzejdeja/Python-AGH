from PIL import Image
from os import listdir
from os.path import splitext
from pathlib import Path

def deleteWords(input, dict):
    for word in dict:
        input = input.replace(word, " ")
    return input
    
dict = ["and", "for", "why", "be"]
for x in range(len(dict)):
    dict[x] = " " + dict[x] + " "
    
path = Path(__file__).parent.absolute()
for e in listdir(path):
    name, ext = splitext(e)
    try:
        if ext.lower() == ".txt":
            f = open(e , "rt")
            for line in f:
                print(deleteWords(line, dict))
            f.close()
    except OSError:
        print("OSError")

