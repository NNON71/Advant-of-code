import re
txt = open("input.txt", "r").read()
x = re.findall(r"mul\(\d{1,3},\d{1,3}\)", txt)
x = ''.join(x)
x = re.findall(r"\d{1,3},\d{1,3}", x)
ans = 0
for i in x :
    a, b = list(map(int, i.split(',')))
    ans += a * b
print(ans)