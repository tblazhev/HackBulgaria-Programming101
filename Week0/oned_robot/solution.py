def final_position(commands, a, b):
    minus_a = -a;
    position = 0
    for command in commands:
        if command == "L" and position > minus_a:
            position -= 1
        elif command == "R" and position < b:
            position += 1
    return position


def main():
    print(final_position("RRLRRLLR", 10, 10))
    print(final_position("RRRRR", 3, 4))
    print(final_position("LLLLLLLLLLR", 2, 6))
    print(final_position(
        "RRRRRRRLRRLRRRRRRRRRRRRLRLRRRRRRRRLRRRRRLRRRRRRRRR", 5, 20))
    print(final_position("RLRLLLLLLLRLLLRLLLLLLLLRLLLLLRLLLRRLLLLLRLLLLLRLLL", 34, 15))

if __name__ == '__main__':
    main()
