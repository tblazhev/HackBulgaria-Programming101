def sum_of_digits(num):
    total = 0
    while num != 0:
        total += (num % 10)
        num = num // 10
    return total

def main():
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))

if __name__ == '__main__':
    main()