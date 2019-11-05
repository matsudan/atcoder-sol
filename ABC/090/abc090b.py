a, b = map(int, input().split())

lst = [1 for i in range(a, b+1) if str(i) == str(i)[::-1]]
print(sum(lst))
