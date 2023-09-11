#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import re,string
def missingCharacters(s):
    # Write your code here
    char=r'[a-z0-9]'
    match=set(re.findall(char,s))
    allchar=set(string.ascii_lowercase+string.digits)
    missing=allchar-match
    return ''.join(sorted(missing))

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
