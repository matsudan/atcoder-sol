a, b = map(int, input().split())
s = input()

if len(s) == a + b + 1 and s[a] == '-':
    ss = s.split('-', 1)
    print('Yes') if len(ss[0]) == a and ss[0].isdecimal and len(ss[1]) == b and ss[1].isdecimal() else print('No')
else:
    print('No')