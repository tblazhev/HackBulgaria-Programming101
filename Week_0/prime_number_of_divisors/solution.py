def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def count_divisors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += 1
    return total

def prime_number_of_divisors(num):
    count = count_divisors(num)
    if is_prime(count):
        return True
    return False

def main():
    print(prime_number_of_divisors(7))
    print(prime_number_of_divisors(8))
    print(prime_number_of_divisors(9))

if __name__ == '__main__':
    main()