from itertools import product

n = input()
ops = product('+-', repeat=3)

for op in ops:
    fm = n[0] + op[0] + n[1] + op[1] + n[2] + op[2] + n[3]
    if eval(fm) == 7:
        print(fm + '=7')
        break
