from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d['A'].append(input())
for i in range(m):
    d['B'].append(input())

for b in d['B']:
    indices = [str(i + 1) for i, a in enumerate(d['A']) if a == b]
    if indices:
        print(' '.join(indices))
    else:
        print(-1)