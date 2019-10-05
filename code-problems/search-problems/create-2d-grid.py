"""
Using list comprehension, create a 2D matrix of 0's
"""

WIDTH = 3
HEIGHT = 5

# In what order does this execute? Left to right? or Right to Left?
# Is it a 3x5 or 5x3 matrix (where row x height)
matrix = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

for row in matrix:
    print(row)
