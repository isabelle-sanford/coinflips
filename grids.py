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

fullgrid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
grid_1move = [[1,1,1,1,1],[0,0,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

#print(possible_moves(grid_1move, False))

def moves_max(grid):
    lost = False
    row = True
    num_moves = 0

    curr_grids = [grid]
    temp_grids = curr_grids.copy()
    next_grids = []

    while lost == False:
        # loop through grids on current step
        print(temp_grids)
        for g in curr_grids:
            #print(g)
            moves = possible_moves(g, row)
            # remove all grids with no next step
            if len(moves) == 0:
                temp_grids.remove(g)
                print("wrong length")
            else:
                # add all next steps to next_grids
                for m in moves:
                    next_grids.append(move(g, m, row))
                    print(next_grids)
                    print(temp_grids)

        #print(f"Grids that have a next step after {num_moves}: {temp_grids}")
        #print(f"Starting grids for step {num_moves + 1}: {next_grids}")
        print("----")

        # reset curr/next/temp
        curr_grids = next_grids
        next_grids = []
        temp_grids = curr_grids
        
        #print(len(curr_grids))

        # check if all moves used up
        if len(curr_grids) > 0:
            num_moves += 1
            row = not row
        else:
            lost = True
        
    
    return num_moves



print(moves_max(gridex))


