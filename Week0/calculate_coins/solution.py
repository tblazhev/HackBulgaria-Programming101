coins = [100, 50, 20, 10, 5, 2, 1]


def calculate_coins(sum):
    int_sum = sum * 100

    num_coins = {}
    for coin in coins:
        count = 0
        while int_sum >= coin:
            int_sum -= coin
            count += 1
        num_coins[coin] = count

    return num_coins


def main():
    print(calculate_coins(0.53))
    print(calculate_coins(8.94))

if __name__ == '__main__':
    main()
