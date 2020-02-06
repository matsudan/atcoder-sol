a, b = map(int, input().split())

aa = ''.join([str(a) for i in range(b)])
bb = ''.join([str(b) for j in range(a)])

lst = [aa, bb]
print(sorted(lst)[0])
