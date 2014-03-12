def magic_string(string):
    k = len(string) // 2
    count_changes = 0
    for index, char in enumerate(string):
        if index < k and char == "<":
            count_changes += 1
        elif index >= k and char == ">":
            count_changes += 1
    return count_changes


def main():
    print(magic_string(">><<><"))
    print(magic_string(">>>><<<<"))
    print(magic_string("<<>>"))
    print(magic_string("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"))


if __name__ == '__main__':
    main()
