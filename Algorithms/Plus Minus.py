#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    sum_positive = 0
    sum_negative = 0
    sum_zero = 0
    
    for number in arr:
        if (number > 0):
            sum_positive += 1
        elif (number < 0):
            sum_negative += 1
        else:
            sum_zero += 1
    
    print(round(sum_positive / len(arr), 6))
    print(round(sum_negative / len(arr), 6))
    print(round(sum_zero / len(arr), 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
