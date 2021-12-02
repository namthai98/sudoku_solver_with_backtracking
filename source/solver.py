import create_grid

def solve(grid):
    find = create_grid.find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0

    return False


def valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True


# print("Original:")
# create_grid.print_grid(create_grid.grid_2)
# solve(create_grid.grid_2)
# print("\nSolved:")
# create_grid.print_grid(create_grid.grid_2)
