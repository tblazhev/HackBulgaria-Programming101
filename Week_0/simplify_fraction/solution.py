def simplify_fraction(fraction):
	nominator = fraction[0]
	denominator = fraction[1]
	min_el = min(nominator, denominator)
	for i in range(2, min_el + 1):
		while nominator % i == 0 and denominator % i == 0:
			nominator //= i
			denominator //= i

	return (nominator, denominator)


def main():
	print(simplify_fraction((3,9)))
	print(simplify_fraction((1,7)))
	print(simplify_fraction((4,10)))
	print(simplify_fraction((63,462)))
	

if __name__ == '__main__':
	main()