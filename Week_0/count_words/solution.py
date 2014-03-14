def count_words(arr):
    word_count = {}

    for word in arr:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    return word_count


def main():
    print(count_words(["apple", "banana", "apple", "pie"]))
    print(count_words(["python", "python", "python", "ruby"]))


if __name__ == '__main__':
    main()