import sys

def get_file_contents(filename):
	fp = open(filename, 'r')
	contents = fp.read()
	fp.close()
	return contents

def main():
	if len(sys.argv) > 1:
		contents = []
		for filename in sys.argv[1:]:
			contents.append(get_file_contents(filename))
		print("\n\n".join(contents))
	else:
		print("No arguments given.")

if __name__ == '__main__':
    main()