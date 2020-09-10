#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict = {}
    for word in magazine:
        if word in mag_dict:
            mag_dict[word] += 1
        else:
            mag_dict[word] = 1

    for word in note:
        if word in mag_dict:
            if mag_dict[word] > 0:
                mag_dict[word] -= 1
            else:
                print("No")
                return ("No")
        else:
            print("No")
            return ("No")
    print("Yes")
    return ("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
