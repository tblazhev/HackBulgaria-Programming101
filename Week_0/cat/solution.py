import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        fp = open(filename, 'r')
        contents = fp.read()
        print(contents)
        fp.close()
    else:
        print("No arguments given.")

if __name__ == '__main__':
    main()
