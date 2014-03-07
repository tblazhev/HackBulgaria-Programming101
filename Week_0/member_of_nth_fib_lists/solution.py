def member_of_nth_fib_lists(listA, listB, needle):
	if needle == listA or needle == listB:
		return True

	a = listA
	b = listB
	index = 2

	len_needle = len(needle)
	while index < len_needle:
		next = b + a
		a = b
		b = next
		index += 1
		if next == needle:
			return True
	return False


def main():
	print(member_of_nth_fib_lists([1, 2], [3, 4], [3, 4, 1, 2, 3, 4]))
	print(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
	print(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))
	print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))


if __name__ == '__main__':
	main()