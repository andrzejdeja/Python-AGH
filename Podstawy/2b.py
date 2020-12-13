from os import listdir
from os.path import isdir, join
def prntdir(path):
    list = listdir(path)
    for f in list:
        if not isdir(join(path, f)):
            print(f)
    for f in list:
        if isdir(join(path, f)):
            prntdir(join(path, f))
try:
    path = "/"
    prntdir(path)
except OSError:
    print("OSError")

