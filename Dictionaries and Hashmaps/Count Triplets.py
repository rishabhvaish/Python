#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countTriplets function below.
def countTriplets(arr, r):
    arr_dict = {}
    left = {}
    for digit in arr:
        if digit in arr_dict:
            arr_dict[digit] += 1
        else:
            arr_dict[digit] = 1

    answer = 0

    for i in arr:
        arr_dict[i] = arr_dict[i] - 1
        if i % r == 0 and i / r in left and i * r in arr_dict:
            answer = answer + (left[i / r] * arr_dict[i * r])
        if i in left:
            left[i] += 1
        else:
            left[i] = 1
    return (answer)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
