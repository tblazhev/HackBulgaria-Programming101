def list_to_number(numList):
	num = 0
	exp = 0
	for item in numList[::-1]:
		num += item * (10 ** exp)
		exp += 1
	return num


def main():
	print(list_to_number([1,2,3]))
	print(list_to_number([9,9,9,9,9]))
	print(list_to_number([1,2,3,0,2,3]))

if __name__ == '__main__':
		main()	
