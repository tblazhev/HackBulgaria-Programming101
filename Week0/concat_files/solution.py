import sys

def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        megatron = open('MEGATRON', 'a')
        contents = []
        for filename in files:
            f = open(filename, 'r')
            contents.append(f.read())
            f.close()
        megatron.write("\n\n".join(contents))
        megatron.close()
    else:
        print("No arguments given.")


if __name__ == '__main__':
    main()
