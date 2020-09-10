#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    answer = []
    arr_dict = Counter()
    count_dict = Counter()
    for o,v in queries:
        if o == 1:
            count_dict[arr_dict[v]] -= 1
            arr_dict[v]+=1
            count_dict[arr_dict[v]] += 1
        elif o == 2:
            if arr_dict[v]>0:
                count_dict[arr_dict[v]] -= 1
                arr_dict[v] -= 1
                count_dict[arr_dict[v]] += 1
        else:
            if count_dict[v]>0:
                answer.append(1)
            else:
                answer.append(0)
    return(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
