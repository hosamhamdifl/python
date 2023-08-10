#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
   
    result_l = 0
    result_r = 0
    for i in range(0, len(arr)):
        for j in range(0,len(arr)):
            if i+j==len(arr)-1:
                result_l+=arr[i][j]
            if i-j==0:
                result_r+=arr[i][j]
    return abs(result_l-result_r)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
