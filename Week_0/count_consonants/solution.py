def count_consonants(string):
	count = 0
	consonants = 'pbcdfghjklmnqrstvwxz'
	for s in string:
		if s.lower() in consonants:
			count += 1
	return count


def main():
	print(count_consonants("Python"))
	print(count_consonants("Theistareykjarbunga")) #It's a volcano name!
	print(count_consonants("grrrrgh!"))
	print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_consonants("A nice day to code!"))


if __name__ == '__main__':
	main()