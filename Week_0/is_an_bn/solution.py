def is_an_bn(word):
    n = len(word)
    if n % 2 != 0:
        return False
    n = n // 2
    check = 'a' * n + 'b' * n
    if word == check:
        return True
    return False

def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    main()