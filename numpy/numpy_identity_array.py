import numpy as np

np.set_printoptions(legacy='1.13')
shape = tuple(map(int, input().split()))

print(np.eye(shape[0],shape[1],k=0))



