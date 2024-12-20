inp = open("input.txt", "r").read()
inp = inp.splitlines()

def loop(target, array) :
    if len(array) == 1 : return target == array[0]
    if target % array[-1] == 0 and loop(target // array[-1], array[:-1]) : return True
    if target > array[-1] and loop(target - array[-1], array[:-1]) : return True
    s_target = str(target)
    s_last = str(array[-1])
    if len(s_target) > len(s_last) and s_target.endswith(s_last) and loop(int(s_target[:-len(s_last)]), array[:-1]) : return True
    return False 

total = 0

for i in inp :
    i = i.split(": ")
    target = int(i[0])
    array = [int(x) for x in i[1].split()]
    if loop(target, array) :
        total += target
print(total)

