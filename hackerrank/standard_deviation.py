#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    res=0
    mean=sum(arr)/len(arr)
    for i in range(len(arr)):
        res+=math.pow((arr[i]-mean),2)
    print(math.sqrt(res//len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
