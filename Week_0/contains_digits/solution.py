def contains_digit(num, digit):
    while num != 0:
        if num % 10 == digit:
            return True
        num //= 10
    return False

def contains_digits(num, digits):
    if len(digits) == 0:
        return True
    for digit in digits:
        if not contains_digit(num, digit):
            return False
    return True


def main():
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6,4]))
    print(contains_digits(123456789, [1,2,3,0]))
    print(contains_digits(456, []))

if __name__ == '__main__':
    main()