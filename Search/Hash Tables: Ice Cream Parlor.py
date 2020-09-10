#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_map = {}
    for i, c in enumerate(cost):
        sunny = c
        johnny = money - c
        if johnny in cost_map.keys():
            print(cost_map[johnny]+1, i+1)
        else:
            cost_map[c] = i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
