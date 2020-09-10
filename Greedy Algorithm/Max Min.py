#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    fairness = arr[k - 1] - arr[0]
    for i in range(1,len(arr) - k + 1):
        print(arr[k+i-1], arr[i])
        fair_current = arr[k+i-1] - arr[i]
        if fair_current < fairness:
            fairness = fair_current
    return fairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
