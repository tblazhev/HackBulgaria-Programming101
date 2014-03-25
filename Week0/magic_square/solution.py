def magic_square(matrix):
    rows_sum = sum(matrix[0])
    len_matrix = len(matrix)

    for row in matrix:
        current_row_sum = sum(row)
        if current_row_sum != rows_sum:
            return False

    col_sums = {}
    last_col_sum = 0
    for i in range(0, len_matrix):
        for j in range(0, len_matrix):
            if i not in col_sums:
                col_sums[i] = matrix[i][j]
            else:
                col_sums[i] += matrix[i][j]
        if i != 0 and last_col_sum != col_sums[i]:
            return False
        last_col_sum = col_sums[i]

    left_diagonal = 0
    right_diagonal = 0
    for i in range(0, len_matrix):
        left_diagonal += matrix[i][i]
        right_diagonal += matrix[len_matrix - i - 1][len_matrix - j - 1]
    if left_diagonal != right_diagonal:
        return False
    return True


def main():
    print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print(magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

if __name__ == '__main__':
    main()
