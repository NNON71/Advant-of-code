inp = open("input.txt", "r").read()
inp = inp.splitlines()

def loop(target, array) :
    if len(array) == 1 : 
        return target == array[0]
    if target % array[-1] == 0 and loop(target // array[-1], array[:-1]) : 
        return True
    if target > array[-1] and loop(target - array[-1], array[:-1]) : 
        return True
    return False 

total = 0

for i in inp :
    i = i.split(": ")
    target = int(i[0])
    array = [int(x) for x in i[1].split()]
    if loop(target, array) :
        total += target
print(total)

