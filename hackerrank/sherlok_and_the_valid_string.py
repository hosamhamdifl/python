#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
   # Count the frequency of each character
   freq = Counter(s)

   # Count the frequency of each frequency
   freq_of_freq = Counter(freq.values())

   # If there is only one type of frequency, it's valid
   if len(freq_of_freq) == 1:
       return 'YES'
   
   # If there are two types of frequencies
   elif len(freq_of_freq) == 2:
       key1, key2 = freq_of_freq.keys()
       # If one frequency is 1 and it appears only once, it's valid
       if key1 == 1 and freq_of_freq[key1] == 1:
           return 'YES'
       if key2 == 1 and freq_of_freq[key2] == 1:
           return 'YES'
       
       # If the difference between two frequencies is 1 and the higher frequency appears only once, it's valid
       if abs(key1 - key2) == 1 and (freq_of_freq[key1] == 1 or freq_of_freq[key2] == 1):
           return str(freq_of_freq)

   # If none of the above conditions are met, it's not valid
   return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
