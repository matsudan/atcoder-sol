import math

n, k = map(int, input().split())
list_a = input()

m = math.ceil((n - 1) / (k - 1))  # (k - 1)*m + 1 >= n
print(m)
