#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highscores = []
    lowscores = []

    for game, score in enumerate(scores):
        if game == 0:
            highscores.append(score)
            lowscores.append(score)
        
        if score < lowscores[-1]:
            lowscores.append(score)
        
        if score > highscores[-1]:
            highscores.append(score)
    
    return len(highscores) - 1, len(lowscores) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
