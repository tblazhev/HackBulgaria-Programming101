def prime_factorization(n):
	primfac = []
	d = 2
	while d*d <= n:
		count = 0
		while (n % d) == 0:
			count += 1
			n //= d
		if count > 0:
			primfac.append((d, count))
		d += 1
	if n > 1:
		primfac.append((n, 1))
	return primfac

def main():
	print(prime_factorization(10))
	print(prime_factorization(14))
	print(prime_factorization(356))
	print(prime_factorization(89))
	print(prime_factorization(1000))	

if __name__ == '__main__':
	main()