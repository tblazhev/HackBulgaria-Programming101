def lines(text):
    lines = text.split("\n")
    return lines


def unlines(elements):
    elements = map(str, elements)
    return "\n".join(elements)


def words(text):
    text_lines = lines(text)
    words = []
    for line in text_lines:
        new_words = line.split(" ")
        words.extend(new_words)
    return words


def unwords(elements):
    return " ".join(elements)


def tabs_to_spaces(string, one_tab_n_spaces=4):
    spaces = " " * one_tab_n_spaces
    return string.replace("\t", spaces)
