#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    ss = str(s)

    height = 0
    height_old = 0
    valley = 0
    for step in ss:
        if step == 'U':
            height = height_old + 1
        elif step == 'D':
            height = height_old - 1

        if height == -1 and height_old == 0:
            valley = valley + 1

        height_old = height

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
