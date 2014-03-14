def sudoku_solved(sudoku):
    len_sudoku = len(sudoku)

    nums = list(range(1, 10))
    
    ### CHECK ROWS ###
    for row in sudoku:
        row = sorted(row)
        if row != nums:
            return False
    
    ### CHECK COLS ###
    cols = dict( (el, []) for el in nums )
    for row in range(0, len_sudoku):
        for col in range(0, len_sudoku):
            cols[col + 1].append(sudoku[row][col])
    
    for col in cols:
        cols[col] = sorted(cols[col])
        if cols[col] != nums:
            return False

    ### CHECK 3X3 SQUARES ###
    squares = dict( (el, []) for el in nums)
    for row in range(0, len_sudoku):
        for col in range(0, len_sudoku):
            if row < 3:
                key = 1
            elif row < 6:
                key = 4
            else:
                key = 7
            if col < 3:
                key += 0
            elif col < 6:
                key += 1
            else:
                key += 2
            squares[key].append(sudoku[row][col])

    for square in squares:
        squares[square] = sorted(squares[square])
        if squares[square] != nums:
            return False

    return True

def main():
    print(sudoku_solved([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4 ,8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5 ,2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
    ]))
    print(sudoku_solved([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]))

if __name__ == '__main__':
    main()