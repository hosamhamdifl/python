import numpy as np
np.set_printoptions(legacy='1.13')
input_string = input().strip()
input_list=input_string.split()
arrayA=[float(x) for x in input_list]
print(np.floor(arrayA))
print(np.ceil(arrayA))
print(np.rint(arrayA))



