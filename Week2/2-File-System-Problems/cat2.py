# cat2.py
import sys


def main():
    if len(sys.argv) > 1:
        arg = 1
        while arg < len(sys.argv):
            filename = sys.argv[arg]
            text_file = open(filename, "r")
            text = text_file.read()
            text_file.close()
            # print(text)
            print(text)
            arg += 1
    else:
        print("No such File in directory")

if __name__ == '__main__':
    main()
