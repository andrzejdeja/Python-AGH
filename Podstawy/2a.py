from os import listdir
from os.path import isdir, join
try:
    filenames = [f for f in listdir("/dev") if not isdir(join("/dev", f))]
    print(len(filenames))
except OSError:
    print("OSError");

