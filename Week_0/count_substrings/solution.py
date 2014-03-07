def count_substrings(haystack, needle):
	count_occurrencies = 0
	len_haystack = len(haystack)
	len_needle = len(needle)
	index = 0
	check = len_haystack - len_needle
	while index <= check:
		if haystack[index: index + len_needle] == needle:
			count_occurrencies += 1
			index = index + len_needle
		else:
			index += 1

	return count_occurrencies

def main():
	print(count_substrings("This is a test string", "is"))
	print(count_substrings("babababa", "baba"))
	print(count_substrings("Python is an awesome language to program in!", "o"))
	print(count_substrings("We have nothing in common!", "really?"))
	print(count_substrings("This is this and that is this", "this")) # "This" != "this"


if __name__ == '__main__':
	main()