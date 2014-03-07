import sys

def main():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		f = open(filename, 'r')
		contents = f.read().split(" ")
		contents = [int(x) for x in contents]
		total = sum(contents)
		print(total)
		f.close()
	else:
		print("No arguments given.")

if __name__ == '__main__':
	main()