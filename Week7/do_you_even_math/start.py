import orm


def welcome():
    print("Welcome to the \"Do you even math?\" game!")
    print("Here are your options:")
    print("- start")
    print("- highscores")


def main_menu():
    welcome()
    command = input("Enter a command> ")

    if command == "start":
        pass

    name = input("Please enter your name to continue: ")
    Score = orm.Score(name=name, score=0)


def main():
    main_menu()


if __name__ == '__main__':
    main()
