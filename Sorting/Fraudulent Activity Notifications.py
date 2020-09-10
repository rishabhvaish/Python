#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
counts = {}


def activityNotifications(expenditure, d):
    notifications = 0
    for i, val in enumerate(expenditure):
        if i >= d:
            med = get_median(counts, d)
            print(med)
            if expenditure[i] >= med:
                notifications += 1
            oldest_day = i - d
            counts[expenditure[oldest_day]] = counts[expenditure[oldest_day]] - 1

        if val not in counts:
            counts[val] = 0
        counts[val] += 1

    return (notifications)


def find(idx):
    s = 0
    for i in range(0, 200):
        freq = 0
        if i in counts:
            freq = counts[i]
        s = s + freq
        if s >= idx:
            return i


def get_median(counts, d):
    med = find(d // 2 + d % 2)

    if d % 2 == 0:
        ret = find(d / 2 + 1)
        return (med + ret)
    else:
        return (med * 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
