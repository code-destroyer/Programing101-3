# generate_numbers.py
import sys
from random import randint


def main():
    p = 1
    text = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        n = sys.argv[2]
        while p <= int(n):
            text += (str(randint(1, 1000)) + " ")
            p += 1
        textfile = open(filename, "w+")
        textfile.write(text.strip())
        textfile.close()
        print(text)
    else:
        print("No such File in directory")

if __name__ == '__main__':
    main()
