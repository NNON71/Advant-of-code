txt = open("input.txt", "r").read()
line = [list(map(int,line.split())) for line in txt.splitlines()]
# print(line)
def safe(levels) :
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    print(diffs)
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs) 
    
ans = 0
print(line)
for level in line :
    if safe(level) :
        ans += 1
print(ans)