s = input()

no = []
for i, ss in enumerate(s):
    if ((i + 1) % 2 == 0 and ss in ('L','U','D')) or ((i + 1) % 2 != 0 and ss in ('R', 'U', 'D')):
        pass
    else:
        no.append(ss)

if len(no) == 0:
    print('Yes')
else:
    print('No')
