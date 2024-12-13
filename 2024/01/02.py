txt = open("input.txt", "r").read()
line = [list(map(int,line.split())) for line in txt.splitlines()]
a1 = []
a2 = []
ans = 0
for a,b in line :
    a1.append(a)
    a2.append(b)

cache = {}
for i in a1:
    if i not in cache :
        c = a2.count(i)
        cache[i] = c
        ans += i * c
    else :
        ans += i * cache[i]
print(ans)
