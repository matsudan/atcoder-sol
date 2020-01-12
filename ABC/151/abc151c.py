n, m = map(int, input().split())  # n: num problem, m: num submit
lst = [input().split() for i in range(m)]

ac = [False] * n
wa = [0] * n

for i in range(m):
    p_i = int(lst[i][0])
    s_i = lst[i][1]
    if s_i == 'AC':
        ac[p_i-1] = True
    else:
        if ac[p_i-1] is False:
            wa[p_i-1] += 1

num_ac = 0
pnlt = 0
for i in range(n):
    if ac[i]:
        num_ac += 1
        pnlt += wa[i]

print(num_ac, pnlt)
