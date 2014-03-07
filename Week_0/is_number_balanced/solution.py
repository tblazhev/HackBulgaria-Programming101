def sum_of_digits(num):
	total = 0
	while num != 0:
		total += (num % 10)
		num = num // 10
	return total
	
def is_number_balanced(num):
	str_num = str(num)
	num_len= len(str_num)
	if num_len == 1:
		return True

	sum_left = 0
	sum_right = 0

	left_part = int(str_num[:num_len // 2])
	if num_len % 2 == 0:
		right_part = int(str_num[num_len // 2:])
	else:
		right_part = int(str_num[(num_len // 2) + 1:])
		
	if sum_of_digits(left_part) == sum_of_digits(right_part):
		return True

	return False


def main():
	print(is_number_balanced(9))
	print(is_number_balanced(11))
	print(is_number_balanced(13))
	print(is_number_balanced(121))
	print(is_number_balanced(4518))
	print(is_number_balanced(28471))
	print(is_number_balanced(1238033))

if __name__ == '__main__':
	main()