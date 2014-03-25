def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def goldbach(num):
    primes = []
    for i in range(2, num // 2 + 1):
        if is_prime(i) and is_prime(num - i):
            primes.append((i, num - i))
    return primes


def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))


if __name__ == '__main__':
    main()
