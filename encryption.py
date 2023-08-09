#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

from collections import defaultdict

def encryption(text):
    text = text.replace(" ","")
    root= math.sqrt(len(text))
    r = math.floor(root)
    c = math.ceil(root)
    d = defaultdict(str)
    for i in range(0,len(text),c):
        sub = text[i:i+c]
        for x in range(len(sub)):
            d[x]+=sub[x]
    return(list(d.values()))



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    print(*result)


    # fptr.write(result + '\n')

    # fptr.close()