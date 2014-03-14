def sort_fractions(fractions):
    if fractions == []: 
        return []
    else:
        pivot = fractions[0]
        pivot_float = pivot[0] / pivot[1]
        lesser = sort_fractions([x for x in fractions[1:] if x[0] / x[1] < pivot_float])
        greater = sort_fractions([x for x in fractions[1:] if x[0] / x[1] >= pivot_float])
        return lesser + [pivot] + greater



def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

if __name__ == '__main__':
    main()