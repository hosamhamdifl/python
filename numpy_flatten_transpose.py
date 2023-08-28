import numpy as np
N, M = map(int, input().split())
array_2d = []
for _ in range(N):
    row = list(map(int, input().split()))
    array_2d.append(row)
array_2d = np.array(array_2d)
print(np.transpose(array_2d))
print(array_2d.flatten())



