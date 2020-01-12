n, k, m = map(int, input().split())
a = list(map(int, input().split()))

res = n * m - sum(a)

if res > k:
    print(-1)
elif res < 0:
    print(0)
elif res >= 0:
    print(res)
