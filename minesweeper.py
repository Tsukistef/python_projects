'''Practical Task 1 - 2D Lists'''
# Create a fuction that takes a grid of # and -
# where each # represents a mine and each - represent a mine free spot.
# Return a grid where each dash is replaced by a digit, indicating the
# number of mines immediately adjacent to the spot.
mine_grid = [ ["-", "-", "-", "#", "#"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "#", "-", "-", "-"],
["-", "-", "-", "-", "-"] ]

def mine_checker(grid):
    rows = grid
    columns = []
    rowIndex = 0
    
    for x in rows:
        
        columns.append(x[rowIndex])
        rowIndex += 1
        
    return columns
        
    
    
    
    
    
    
    
    
    # coordinates = [(grid[row-1][col]),        # North
    #                (grid[row+1][col]),        # South
    #                (grid[row][col-1]),        # West
    #                (grid[row][col+1]),        # East
    #                (grid[row-1][col-1]),      # North-West
    #                (grid[row-1][col+1]),      # North-East
    #                (grid[row+1][col-1]),      # South-West
    #                (grid[row+1][col+1])]      # South-East
                  
    # for row in range(rows):
    #     for col in row:
    #        if grid[row][col] == '-':
    #            counter = 0
    #            for n in coordinates:
    #                if coordinates[n] == '#':
    #                    counter += 1
    #     grid[row][col] = counter
    # print(grid)
    
mine_checker(mine_grid)