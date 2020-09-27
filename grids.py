# MAKE GRIDS


def flip(row):
    flipped = [(r+1) % 2 for r in row]
    return flipped

ex1 = [0,1,1,0,1]
ex2 = [1, 1, 0, 0, 0]

print(flip(ex2))
