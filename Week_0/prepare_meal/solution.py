def prepare_meal(number):
    string = ''
    spam = []

    n = 0
    while number % 3 == 0:
        n += 1
        number //= 3
    spam += ['spam'] * n

    if number % 5 == 0:
        if not spam:
            spam.append('eggs')
        else:
            spam.append('and eggs')
    return " ".join(spam)

def main():
    print(prepare_meal(5))
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(15))
    print(prepare_meal(45))
    print(prepare_meal(7))


if __name__ == '__main__':
    main()