def sum_of_divisors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += i
    return total


def main():
    print(sum_of_divisors(7))
    print(sum_of_divisors(1000))

if __name__ == '__main__':
    main()
