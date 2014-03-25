import sys
from random import randint


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        n = int(sys.argv[2])
        f = open(filename, 'w')
        numbers = []
        for i in range(0, n):
            numbers.append(str(randint(1, 1000)))
        f.write(" ".join(numbers))
        f.write("\n")
        f.close()
    else:
        print("No arguments given.")

if __name__ == '__main__':
    main()