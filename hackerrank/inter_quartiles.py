#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def median(q):
    if isinstance(q, int):
        return q
    n = len(q)
    if n % 2 == 0:
        return (q[n//2-1]+q[n//2])/2
    else:
        return q[n//2]


def quartiles(arr):
    arr.sort()
    n = len(arr)
    m1 = 0
    m2 = 0
    m3 = 0
    m1 = median(arr[0:n//2])
    if n % 2 == 0:
        m3 = median(arr[n//2:n])
        m2 = median(arr)
    else:
        m3 = median(arr[(n//2)+1:n])
        m2 = median(arr[n//2])

    return int(m1), int(m3-m1), int(m3)


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    res = []
    for i in range(len(values)):
        res += [values[i]] * freqs[i]
    m1, m2, m3 = quartiles(res)
    print(float(m2))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
