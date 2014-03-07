def number_to_list(num):
	num_list = []
	while num != 0:
		num_list.insert(0, num % 10)
		num = num // 10
	return num_list


def main():
	print(number_to_list(123))
	print(number_to_list(99999))
	print(number_to_list(123023))

if __name__ == '__main__':
	main()