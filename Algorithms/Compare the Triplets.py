#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]
    
    alice_points = 0
    bob_points = 0
    
    for n1, n2 in zip(alice, bob):
        if (n1 > n2):
            alice_points += 1
        elif (n1 < n2):
            bob_points += 1
    
    return alice_points, bob_points

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


