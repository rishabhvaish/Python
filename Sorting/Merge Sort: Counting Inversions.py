#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    n = len(arr)
    if n == 1:
        return 0
    left_len = n//2
    right_len = n - left_len
    left = arr[:left_len]
    right = arr[left_len:]
    inversions = countInversions(left) + countInversions(right)

    left_pointer = 0
    right_pointer = 0
    for i in range(n):
        if left_pointer < left_len and (right_pointer >= right_len or left[left_pointer]<=right[right_pointer]):
            arr[i] = left[left_pointer]
            inversions += right_pointer
            left_pointer += 1
        elif right_pointer < right_len:
            arr[i] = right[right_pointer]
            right_pointer += 1
    return inversions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
