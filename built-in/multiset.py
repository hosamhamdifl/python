#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    def __init__(self):
        super().__init__()
        self.val = []

    def add(self, val):
        self.val.append(val)

    def remove(self, val):
        if val in self.val:
            self.val.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.val

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.val)


if __name__ == '__main__':

    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
