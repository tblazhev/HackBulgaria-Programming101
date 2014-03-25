import string_utils
import sys
import os


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("File does not exist")
            return
        f = open(filename, "r+")
        contents = f.read()
        f.seek(0)
        contents_with_spaces = string_utils.tabs_to_spaces(contents)
        f.write(contents_with_spaces)
        f.close()
    else:
        print("No filename given.")


if __name__ == '__main__':
    main()
