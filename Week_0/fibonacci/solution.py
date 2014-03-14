def nth_fibonacci(n):
    a = 1
    b = 1
    index = 2

    while index < n:
        next = a + b
        a = b
        b = next
        index = index + 1
        
    return b

def main():
    print(nth_fibonacci(100))
    print(nth_fibonacci(2))

if __name__ == '__main__':
    main()