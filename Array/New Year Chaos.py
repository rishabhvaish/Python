#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    #lets make index and value same for intuition.
    q = [value - 1 for value in q]
    steps = 0
    for i, val in enumerate(q):
        diff = val - i
        if diff > 2:
            print("Too chaotic")
            return False
        for j in range(max(val -1 , 0),i):
            if q[j] > val:
                steps = steps + 1
    print(steps)
    return True


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
