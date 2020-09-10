#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    set_arr = set(arr)
    if len(set_arr) < len(arr):
        return 0
    set_arr = sorted(set_arr)
    ans = abs(set_arr[0] - set_arr[1])
    for i in range(1,len(set_arr) - 1):
        min_now = abs(set_arr[i] - set_arr[i+1])
        if min_now < ans:
            ans = min_now
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
