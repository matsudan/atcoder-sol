n = int(input())
list_a = sorted(list(map(int, input().split())))[::-1]

print(sum(list_a[0::2]) - sum(list_a[1::2]))
