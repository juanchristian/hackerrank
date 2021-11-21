#!/bin/python3

import sys

def simpleArraySum(n, ar):
    total = 0
    for item in ar:
        total += item
    
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
