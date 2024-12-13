txt = open("input.txt", "r").read()
line = [list(map(int,line.split())) for line in txt.splitlines()]
a1 = []
a2 = []
for a,b in line :
    a1.append(a)
    a2.append(b)
a1.sort()
a2.sort()
for i in range(len(line)) :
    print(a1[i], a2[i], end='\n')

print(sum(list(abs(a1[i] - a2[i]) for i in range(len(line)))))  