def count_numbers(numbers, count_rec = 0):
	# numbers = sorted(numbers, reverse = True)
	numbers.sort(reverse = True)
	new_numbers = []

	for i in range(0, len(numbers)):
		for j in range(i + 1, len(numbers)):
			if numbers[j] == 0:
				continue
			mod = numbers[i] // numbers[j]
			if mod not in numbers and mod not in new_numbers:
				new_numbers.append(mod)

	numbers.extend(new_numbers)
	if len(new_numbers) > 0:
		count_rec += 1
		count_numbers(numbers, count_rec)

	return len(numbers)


def main():
	print(count_numbers([9, 2]))
	print(count_numbers([8, 2]))
	print(count_numbers([50]))
	print(count_numbers([1, 5, 8, 30, 15, 4]))
	print(count_numbers([1, 2, 4, 8, 16, 32, 64]))
	print(count_numbers([6, 2, 18]))


if __name__ == '__main__':
	main()
