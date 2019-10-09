n, m = map(int, input().split())

t = m * 1900 + (n-m) * 100
print(int(t/(1/2)**m))
