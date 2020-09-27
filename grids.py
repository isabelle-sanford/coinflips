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

gridex = [[0, 1, 1, 1, 0], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 0, 1, 1]]

ex1 = [0,1,1,0,1]
ex2 = [1, 1, 0, 0, 0]

def possible_moves(grid, row):
    gridsize = len(grid)
    
    if row == False:
        grid = list(zip(*grid))

    possible = [g for g in range(0,gridsize) if (sum(grid[g]) < (gridsize / 2))]
    
    return possible

def moves_max(grid):
    lost = False
    row = True
    gridp = grid
    num_moves = 0

    curr_grids = grid

    while lost == False:
        move = possible_moves(gridp, row)
        if len(move) == 0:
            # lost
        elif len(move) == 1:
            move(gridp, move, row)
            # add to counter
        else:
            currtree = dict(grids=gridp, moves=move,turn=row)
            for m in move:
                move(gridp, m, row)
