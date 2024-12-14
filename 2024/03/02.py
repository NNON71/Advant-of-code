import re
txt = open("input.txt", "r").read()
ans = 0
on = True
for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", txt) :
    if match == 'do()':
        on = True
    elif match == "don't()":
        on = False
    elif on:
        a, b = map(int, match[4:-1].split(',')) 
        ans += a * b

print(ans)