import numpy as np
shapeA = tuple(map(int, input().split()))
arrayA = []
# shapeB=tuple(map(int, input().split()))
arrayB = []
for _ in range(shapeA[0]):
    row = list(map(int, input().split()))
    arrayA.append(row)
for _ in range(shapeA[0]):
    row = list(map(int, input().split()))
    arrayB.append(row)
print(np.add(arrayA, arrayB))
print(np.subtract(arrayA, arrayB))
print(np.multiply(arrayA, arrayB))
print(np.floor_divide(arrayA, arrayB))
print(np.mod(arrayA, arrayB))
print(np.power(arrayA, arrayB))
