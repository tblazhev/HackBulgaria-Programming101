def is_int_palindrom(num):
    if str(num) == str(num)[::-1]:
        return True
    return False


def main():
    print(is_int_palindrom(1))
    print(is_int_palindrom(42))
    print(is_int_palindrom(100001))
    print(is_int_palindrom(999))
    print(is_int_palindrom(123))

if __name__ == '__main__':
    main()
