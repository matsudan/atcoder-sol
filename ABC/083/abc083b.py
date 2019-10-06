n, a, b = map(int, input().split())

t = 0
for i in range(a, n + 1):
    if a <= sum(map(int, str(i))) <= b:
        t += i
print(t)
