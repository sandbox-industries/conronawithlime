from timeit import default_timer
from tqdm import trange


def read_sudoku():

    path = r'C:\Users\adria\conronawithlime\p096_sudoku.txt'
    grid_list = list()

    with open(path) as s:
        puzzles = s.readlines()
        # Strip newline characters
        puzzles = [line.strip('\n') for line in puzzles]
        # Delete grid markers every 10th element
        del puzzles[0::10]
        # Split each puzzle into ints own list, changing str to int
        for idx in range(0, len(puzzles), 9):
            grid_list.append([list(map(int, num)) for num in puzzles[idx:idx+9]])

    return grid_list


def get_possible(y, x, puzzle):

    possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    column = puzzle[y]
    row = [position[x] for position in puzzle]
    grid_y, grid_x = 3*(y//3), 3*(x//3)

    grid = set()
    for i in range(3):
        for j in range(3):
            grid.add(puzzle[grid_y+i][grid_x+j])

    return possible - set(column) - set(row) - set(grid)


def solve(puzzle):

    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                p = get_possible(y, x, puzzle)
                for num in p:
                    puzzle[y][x] = num
                    if solve(puzzle):
                        return True
                    puzzle[y][x] = 0

                return

    return True


solution = 0
sudokus = read_sudoku()
pbar = trange(len(sudokus))
start = default_timer()
solution = 0

for sudoku in sudokus:

    # print(sudoku)
    solve(sudoku)
    # print(sudoku)
    solution += int(''.join((str(i) for i in sudoku[0][:3])))
    pbar.update(1)

stop = default_timer()
print(solution)
print(stop-start)
