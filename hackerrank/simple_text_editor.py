q = int(input())
s = ''
p_s = []
for _ in range(q):
    ops = list(map(str, input().split()))
    if ops[0] == '1':
        p_s.append(s)
        s += ops[1]
    elif ops[0] == '2':
        p_s.append(s)
        s = s[:-int(ops[1])]
    elif ops[0] == '3':
        print(s[int(ops[1])-1])
    elif ops[0] == '4':
        s = p_s.pop()