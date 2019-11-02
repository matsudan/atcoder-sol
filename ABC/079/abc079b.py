n = int(input())

lst = [2, 1]
[lst.append(lst[i - 1] + lst[i - 2]) for i in range(2, n + 1)]

print(lst[n])
