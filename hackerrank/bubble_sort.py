#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    x=0
    for i in range(0,len(a)):
        numberOfSwaps=0
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                numberOfSwaps+=1
        x+=numberOfSwaps
        if numberOfSwaps==0:
            break
    print(f"Array is sorted in {x} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    
    
        
