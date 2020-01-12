n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = list(map(int, input().split()))

before = n
result = 0
for i in range(n):
    result += list_b[list_a[i] - 1]
    if before + 1 == list_a[i] - 1:
        result += list_c[before]
    before = list_a[i] - 1
print(result)
