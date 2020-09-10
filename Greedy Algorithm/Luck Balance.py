#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck_total = sum(row[0] for row in contests)
    luck_important = []
    for row in contests:
        if row[1] == 1:
            luck_important.append(row[0])
    luck_important.sort()
    diff = len(luck_important) - k
    if diff > 0:
        luck_reduce = sum(luck_important[:diff])
        luck_total = luck_total - 2*luck_reduce
    return luck_total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
