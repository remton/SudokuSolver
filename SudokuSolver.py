# Remington Ward
# 08/10/2020
# SudokuSolver.py
# Takes any sudoku game and solves it if possible
import numpy
import time


class Sudoku:
    def __init__(self, board):
        self.board = board.copy()
        self.solve_attempts = 0
        self.solved_board = []

    @staticmethod
    def print_board(board):
        output = ('=' * 37)
        for y in range(len(board)):
            output += '\n|'
            for x in range(len(board[0])):
                num = board[y][x]
                if num != 0:
                    output += f' {num} '
                else:
                    output += '   '
                if (x + 1) % 3 == 0:
                    output += '|'
                else:
                    output += ' '
            if (y + 1) % 3 == 0:
                output += '\n' + ('=' * 37)
        print(output)

    # returns the amount of possible moves for this index
    def choice_count(self, index):
        y = index[0]
        x = index[1]
        choices = 0
        for num in range(1, 10):
            if self.possible_move(num, index):
                choices += 1
        return choices

    # returns all indexes of self.board sorted by the amount of different choices for the index
    def sorted_indexes(self):
        board = self.board
        indexes = []
        choices = []
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    choices.append(self.choice_count([y, x]))
                    indexes.append([y, x])
        indexes_array = numpy.asarray(indexes)
        choices_array = numpy.asarray(choices)
        inds = choices_array.argsort()
        sorted_indexes = indexes_array[inds]
        return sorted_indexes

    def possible_move(self, num, index):
        board = self.board
        y = index[0]
        x = index[1]
        # row check
        for i in range(0, 9):
            if board[y][i] == num:
                return False
        # column check
        for i in range(0, 9):
            if board[i][x] == num:
                return False
        # box check
        # Note: '//' returns the floor of the division result
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if board[y0 + i][x0 + j] == num:
                    return False
        return True

    def solve(self):
        self.solve_attempts += 1
        board = self.board
        for index in self.sorted_indexes():
            y = index[0]
            x = index[1]
            if board[y][x] == 0:
                for num in range(1, 10):
                    if self.possible_move(num, [y, x]):
                        board[y][x] = num
                        if self.solve():
                            return True
                        board[y][x] = 0
                return False

        self.solved_board = board.copy()
        return True


# grid = [[5, 3, 0,   0, 7, 0,   0, 0, 0],
#         [6, 0, 0,   1, 9, 5,   0, 0, 0],
#         [0, 9, 8,   0, 0, 0,   0, 6, 0],

#         [8, 0, 0,   0, 6, 0,   0, 0, 3],
#         [4, 0, 0,   8, 0, 3,   0, 0, 1],
#         [7, 0, 0,   0, 2, 0,   0, 0, 6],

#         [0, 6, 0,   0, 0, 0,   2, 8, 0],
#         [0, 0, 0,   4, 1, 9,   0, 0, 5],
#         [0, 0, 0,   0, 8, 0,   0, 7, 9]]

grid = [[0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],

        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],

        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0]]

sudoku = Sudoku(grid)
sudoku.print_board(sudoku.board)
start_time = time.time()
is_solved = sudoku.solve()
end_time = time.time()
calc_time = end_time - start_time
print(f'\nDid we get a solution? {is_solved}')
if is_solved:
    print(f'solved in {calc_time} seconds \nwith {sudoku.solve_attempts} calls of sudoku.solve()')
    Sudoku.print_board(sudoku.solved_board)
