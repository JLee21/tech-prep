"""
Given a 2D grid, count the number of islands, where 1 denotes island and 0 denotes
water. Islands can be connected in cardinal directions (up, down, left, right)
"""

# one island
grid = [[0, 0, 0],
        [0, 1, 1],
        [0, 0, 1]]
# two islands
grid2 = [[0, 0, 0],
         [0, 1, 1],
         [1, 0, 1]]
#  one island
grid3 = [[0, 0, 1],
         [1, 1, 1],
         [1, 0, 1]]
#  zero islands
grid4 = [[0]]
# one island
grid5 = [[1]]


def countIslandDFS(grid):
    cnt = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                search(row, col, grid)
                cnt += 1
    return cnt


def search(row, col, grid):
    # check bounds
    if row < 0 or row > len(grid)-1:
        return
    if col < 0 or col > len(grid[0])-1:
        return
    if grid[row][col] == 0:
        return
    # mark as visited
    grid[row][col] = 0
    # explore new land depth first
    search(row-1, col, grid)  # up
    search(row+1, col, grid)  # down
    search(row, col-1, grid)  # left
    search(row, col+1, grid)  # right


assert countIslandDFS(grid) == 1
assert countIslandDFS(grid2) == 2
assert countIslandDFS(grid3) == 1
assert countIslandDFS(grid4) == 0
assert countIslandDFS(grid5) == 1
