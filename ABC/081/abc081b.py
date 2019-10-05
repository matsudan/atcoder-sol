n = int(input())
list_n = list(map(int, input().split()))

c = 0
while all(i % 2 == 0 for i in list_n):
    list_n = [i/2 for i in list_n]
    c += 1

print(c)
