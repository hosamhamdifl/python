#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
   
    dict_h={
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine",
        "10":"ten",
        "11":"eleven",
        "12":"twelve"
    }
    dict_m={
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine",
        "10":"ten",
        "11":"eleven",
        "12":"twelve",
        "13":"thirteen",
        "14":"fourteen",
        "15":"quarter",
        "16":"sixteen",
        "17":"seventeen",
        "18":"eighteen",
        "19":"nineteen",
        "20":"twenty",
        "21":"twentyone",
        "22":"twentytwo",
        "23":"twentythree",
        "24":"twentyfour",
        "25":"twentyfive",
        "26":"twentysix",
        "27":"twentyseven",
        "28":"twentyeight",
        "29":"twentynine",
        "30":"half past ",

    }
    result=""
    past=" past "
    minute=" minutes"
    to=" to "
    if m<30 or m>=1 :
        if m==15:
            result=dict_m[str(m)] +past
        elif m==0:
            result=""
       
        elif m==30:
            result=dict_m[str(m)]
        elif m-30==15:
            result=dict_m[str(m-30)]+to
        elif m>30:
            result=dict_m[str(60-m)] +minute+to
        else:
            result=dict_m[str(m)] +minute+past

    
    # if m-30>0:
    #     result=dict_m[str(60-m)]+minute+to
    if h<=12 or h>=1 and m<=30:
        if m==0 or str(m)=="00":
            result+=dict_h[str(h)]+" o\' clock"
        elif m<=30:
            result+=dict_h[str(h)]
        elif m>30:
            result+=dict_h[str(h+1)]
    
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
