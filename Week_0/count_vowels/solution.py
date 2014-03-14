def count_vowels(string):
    count = 0
    vowels = 'aeiouy'
    for s in string:
        if s.lower() in vowels:
            count += 1
    return count


def main():
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))  # It's a volcano name!
    print(count_vowels("grrrrgh!"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))


if __name__ == '__main__':
    main()
