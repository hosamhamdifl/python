import numpy as np

n = int(input())
a = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(a), 2))
