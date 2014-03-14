def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB

    a = listA
    b = listB
    index = 2

    while index < n:
        next = b + a
        a = b
        b = next
        index += 1

    return b


def main():
    print(nth_fib_lists([1,2], [3,4], 4))

    print(nth_fib_lists([1], [2], 1))
    print(nth_fib_lists([1], [2], 2))
    print(nth_fib_lists([1, 2], [1, 3], 3))
    print(nth_fib_lists([], [1, 2, 3], 4))
    print(nth_fib_lists([], [], 100))

if __name__ == '__main__':
    main()