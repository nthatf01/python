grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(grid[i][j], end = '')
    print('')

for i in range(len(grid[0])):
    for j in range(8):
        print(grid[j][i], end = '')
    print('')

