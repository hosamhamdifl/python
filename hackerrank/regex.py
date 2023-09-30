#!/bin/python3

import math
import os
import random
import re
import sys


def print_order_email(emails):
    exp='gmail'
    res=[]
    for i in emails:
        if re.search(r'@gmail.com',i[1]):
            res.append(i[0])
    print('\n'.join(sorted(res)))
    
if __name__ == '__main__':
    N = int(input().strip())
    emails=[]

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        emails.append([firstName,emailID])
    print_order_email(emails)
        
