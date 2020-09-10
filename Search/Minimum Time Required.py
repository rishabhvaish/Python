#!/bin/python3

import math
import os
import random
import re
import sys
from math import ceil


# Complete the minTime function below.
def minTime(machines, goal):
    machines.sort()
    n = len(machines)
    maximum = ceil(goal / n) * machines[n - 1]
    minimum = ceil(goal / n) * machines[0]
    while minimum + 1 < maximum:
        mid = (minimum + maximum) // 2
        produce = sum([mid // day for day in machines])
        print(minimum, maximum, mid, produce)
        if produce < goal:
            minimum = mid
        else:
            maximum = mid

    produce = sum([minimum // day for day in machines])
    if produce == goal:
        return minimum
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
