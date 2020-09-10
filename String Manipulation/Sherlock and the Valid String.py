#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    char_dic = {}
    for char in s:
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1

    max_count = char_dic[char]
    min_count = char_dic[char]
    count_dic = {}
    for elem, count in char_dic.items():
        if count in count_dic:
            count_dic[count] += 1
        else:
            count_dic[count] = 1

        if count > max_count:
            max_count = count
        if count < min_count:
            min_count = count

    if len(count_dic) == 1:
        return ("YES")
    if len(count_dic) == 2:
        if count_dic[max_count] == 1 and max_count - min_count == 1:
            return ("YES")
        elif count_dic[min_count] == 1 and min_count == 1:
            return ("YES")
    return ("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
