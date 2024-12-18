grid = open("input.txt", "r").read()
grid = list(map(list, grid.splitlines()))

rows = len(grid)
cols = len(grid[0])
r, c = 0, 0 
for i in range(rows) :
    for j in range(cols) :
        if grid[i][j] == '^' :
            r, c = i, j
            break

dr = -1
dc = 0

seen = set()

while True :
    seen.add((r, c))
    if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dr >= cols : break
    if grid[r + dr][c + dc] == '#' :
        dc, dr = -dr, dc
    else :
        r += dr
        c += dc
    
print(len(seen))