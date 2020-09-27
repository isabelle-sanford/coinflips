# MAKE GRIDS


def flip(row):
    flipped = [(r+1) % 2 for r in row]
    return flipped


def move(grid, index, row):
    if row == False:
        grid = list(zip(*grid))
        
    grid[index] = flip(grid[index])

    if row == False:
        grid = list(zip(*grid))
        grid = [list(r) for r in grid]

    return grid

gridex = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]

ex1 = [0,1,1,0,1]
ex2 = [1, 1, 0, 0, 0]


