#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swapCount = 0
    for i in range(len(a)):
        swapped = False
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                swapCount+=1
        if not swapped:
            break
    print('Array is sorted in ' + str(swapCount) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[len(a)-1]))
    return 0
                

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
