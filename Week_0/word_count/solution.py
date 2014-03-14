import sys


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        filename = sys.argv[2]
        f = open(filename, 'r');
        contents = f.read();
        f.close()

        if command == 'chars':
            print(len(contents))
        elif command == 'words':
            words = contents.split(" ");
            print(len(words))
        elif command == 'lines':
            lines = contents.split("\n")
            print(len(lines))
    else:
        print("No arguments given.")


if __name__ == '__main__':
    main()