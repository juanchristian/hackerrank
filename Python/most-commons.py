#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict


def do_stuff(word: str):
    letters = Counter(sorted(word)).most_common(3)
    for letter, count in letters:
        print(letter, count)


if __name__ == '__main__':
    s = input()
    do_stuff(str.lower(s))
