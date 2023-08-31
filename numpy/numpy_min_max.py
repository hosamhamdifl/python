import numpy as np

shape=tuple(map(int,input().split()))
arrayA=[]
for _ in range(shape[0]):
    row = list(map(int,input().split()))
    arrayA.append(row)
arrayB=np.reshape(arrayA,shape)
arrayC=np.min(arrayB,axis=1)
print(np.max(arrayC))



