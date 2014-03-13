from glob import glob
import sys


def main():
    if len(sys.argv) > 2:
        ext = sys.argv[1]
        search_dir = sys.argv[2]
        pattern = search_dir + "*." + ext
        files = glob(pattern)
        print(len(files))
    else:
        print("No extension and/or directory given.")


if __name__ == '__main__':
    main()
