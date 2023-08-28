import numpy
n, m, p = map(int, input().split())

array1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    array1.append(row)

array2 = []
for _ in range(m):
    row = list(map(int, input().split()))
    array2.append(row)

carray = numpy.concatenate((array1, array2), axis=0)
print(carray)
