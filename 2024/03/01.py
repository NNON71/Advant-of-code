import re
txt = open("input.txt", "r").read()
ans = 0
for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", txt):
    a, b = map(int, match) 
    ans += a * b

print(ans)