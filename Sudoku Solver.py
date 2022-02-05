# You can change the grid according to the puzzle (a sample grid is given)

grid = [
        [8, 0, 7, 0, 0, 9, 6, 0, 5],
        [0, 0, 3, 0, 2, 0, 8, 0, 0],
        [0, 5, 1, 7, 0, 0, 2, 3, 9],
        [2, 4, 0, 0, 1, 6, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 5, 3, 0, 0, 8, 4],
        [0, 1, 9, 0, 0, 4, 7, 6, 0],
        [0, 0, 4, 0, 7, 0, 3, 0, 0],
        [7, 0, 2, 8, 0, 0, 4, 0, 1]
        ]

def print_grid():
    global grid
    for li in grid:
        print(li)

# This function determines whether a number (1 to 9) can be placed at a certain position in the grid
# by checking its uniqueness in its respective row, column, and box

def is_possible(y, x, num):
    global grid
    row = grid[y]
    column = []
    box = []
    for li in grid:
        column.append(li[x])
    x_box = (x//3)*3
    y_box = (y//3)*3
    for i in range(3):
        for j in range(3):
            box.append(grid[y_box+i][x_box+j])
    if num not in row and num not in column and num not in box:
        return True
    else:
        return False

# The final solve function (it uses recursion and backtracking)

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for num in range(1, 10):
                    if is_possible(y, x, num) == True:
                        grid[y][x] = num
                        solve() # Resursion
                        grid[y][x] = 0 # Backtracking (because the fuction coming to this line intead to going to line <55> means that choosing this particular value caused us to reach at a dead end, i.e. no values for a particular blank cell works)
                        
                return
    
    print_grid() # The only way of coming here is if our grid is filled. So, a solution has been found and thus it gets printed.
    print("")
    input() # It enter key is pressed, the program continues the recursion and searches for more solutions until all possible combinations has been tried.

# Solving the puzzle
solve()
