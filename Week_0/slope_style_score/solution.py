def average(arr):
    total = 0
    for item in arr:
        total += item
    return total / len(arr)

def slope_style_score(scores):
    scores = sorted(scores)
    return round(average(scores[1:-1]), 2)


def main():
    print(slope_style_score([94, 95, 95, 95, 90]))
    print(slope_style_score([60, 70, 80, 90, 100]))
    print(slope_style_score([96, 95.5, 93, 89, 92]))

if __name__ == '__main__':
    main()