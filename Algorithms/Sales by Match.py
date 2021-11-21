#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = defaultdict(int)
    for item in ar:
        socks[item] += 1

    result = 0
    for key, value in socks.items():
            result += int(value / 2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
