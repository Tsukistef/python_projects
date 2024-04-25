'''Practical Task 1 - 2D Lists'''
# Create a fuction that takes a grid of '#' and '-'
# where each # represents a mine and each - represent a mine free spot.
# Return a grid where each dash is replaced by a digit, indicating the
# number of mines immediately adjacent to the spot.

def mine_checker(grid):
    # Create a new grid to store the results
    new_grid = []
    
    # Iterate through each row in the grid
    for row in range(len(grid)):
        new_row = []
        # Iterate through each column in the row
        for col in range(len(grid[row])):
            counter = 0
            # Check if the current cell is a mine
            if grid[row][col] == '-':
                # Check the surrounding cells
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # Skip the current cell
                        if i == 0 and j == 0:
                            continue
                        # Check if the adjacent cell is within the grid boundaries
                        if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[row]):
                            # Increment the counter if the adjacent cell is a mine
                            if grid[row + i][col + j] == '#':
                                counter += 1
                new_row.append(counter)
            else:
                # If the current cell is already a mine, append '#' to the new grid
                new_row.append('#')
        new_grid.append(new_row)
    
    return new_grid

# Example:
mine_grid = [ ["-", "-", "-", "#", "#"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "#", "-", "-", "-"],
["-", "-", "-", "-", "-"] ]

result = mine_checker(mine_grid)
for row in result:
    print(row)
