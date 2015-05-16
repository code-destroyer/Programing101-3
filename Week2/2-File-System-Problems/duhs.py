import sys
import os


def duhs():
    size = 0
    path = sys.argv[1]
    try:
        for (path, dirs, files) in os.walk(path):
            for file in files:
                filename = os.path.join(path, file)
                size += os.path.getsize(filename)
        return size
    except OSError as error:
        print(error)

print(duhs())
