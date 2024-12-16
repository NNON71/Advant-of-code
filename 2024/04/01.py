txt = open("input.txt", "r").read()
grid = [[word for word in line] for line in txt.splitlines()]
count = 0
for row in range(len(grid)) :
    for col in range(len(grid[0])) :
        if grid[row][col] != 'X' : continue
        for dy in [-1, 0, 1] :
            for dx in [-1, 0 , 1] : 
                if dx == dy == 0 : continue
                if not (0 <= row + 3 * dy < len(grid) and 0 <= col + 3 * dx < len(grid[0])) : continue
                if grid[row + dy][col + dx] == 'M' and grid[row + dy * 2][col + dx * 2] == 'A' and grid[row + dy * 3][col + dx * 3] == 'S' :
                    count += 1
                 
print(count)