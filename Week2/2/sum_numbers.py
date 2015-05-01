import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        text_file = open(filename, "r")
        text = text_file.read()
        values = text.split(" ")
        sum = 0
        for element in range(0, len(values)):
            sum += int(values[int(element)])
        text_file.close()
        print(sum)
    else:
        print("No such File in directory")

if __name__ == '__main__':
    main()
