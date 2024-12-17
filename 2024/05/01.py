txt = open("input.txt", "r").read()
txt = txt.splitlines()

rule = []
for line in txt :
    if line.isspace(): break 
    elif line == '' : break
    rule.append(list(map(int, line.split('|'))))


cache = {}

for x, y in rule :
    cache[(x, y)] = True
    cache[(y, x)] = False

def is_order(update) :
    for i in range(len(update)):
        for j in range(i + 1, len(update)) :
            key = (update[i], update[j])
            if key in cache and not cache[key] :
                return False
    return True

total = 0

for line in txt :
    if line == '' or line[2] == '|' : continue
    update = list(map(int, line.split(',')))
    if is_order(update) :
        total += update[len(update) // 2]
        
print(total)
