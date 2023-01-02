#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    cur_idx = n-1
    low_idx = n-2
    value=arr[cur_idx] 
    for i in range(n):    
        if value > arr[low_idx] or i==n-1:
            arr[cur_idx]=value
            print(*arr)
            break
        else:
            arr[cur_idx]=arr[low_idx]
            cur_idx-=1
            low_idx-=1
            print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
