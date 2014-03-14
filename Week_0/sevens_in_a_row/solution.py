def sevens_in_a_row(arr, n):
    count_sevens = 0
    for item in arr:
        if item == 7:
            count_sevens += 1
        else:
            count_sevens = 0
        if count_sevens == n:
            return True
    return False

def main():
    print(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
    print(sevens_in_a_row([1,7,1,7,7], 4))
    print(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
    print(sevens_in_a_row([7,2,1,6,2], 1))

if __name__ == '__main__':
    main()
