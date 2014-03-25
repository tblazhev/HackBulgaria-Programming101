def sum_of_min_and_max(numArr):
    numArr.sort()
    return numArr[0] + numArr[len(numArr) - 1]


def main():
    print(sum_of_min_and_max([1, 2, 3]))
    print(sum_of_min_and_max([-10, 5, 10, 100]))

if __name__ == '__main__':
    main()
