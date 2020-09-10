#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_dict = {}
    for letter in s1:
        if letter in s1_dict:
            s1_dict[letter] += 1
        else:
            s1_dict[letter] = 1

    for letter in s2:
        if letter in s1_dict:
            print("YES")
            return ("YES")

    print("NO")
    return ("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
