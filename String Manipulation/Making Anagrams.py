#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_dic = {}
    for char in a:
        if char in a_dic:
            a_dic[char] += 1
        else:
            a_dic[char] = 1

    b_dic = {}
    for char in b:
        if char in b_dic:
            b_dic[char] += 1
        else:
            b_dic[char] = 1

    answer = 0
    for elem in b_dic:
        if elem in a_dic:
            answer += abs(a_dic[elem] - b_dic[elem])
            a_dic[elem] = 0
        else:
            answer += b_dic[elem]

    return answer + sum(a_dic.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
