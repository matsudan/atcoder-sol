n = int(input())
list_s = list(input().split())

length = len(set(list_s))

if length == 3:
    print('Three')

if length == 4:
    print('Four')
