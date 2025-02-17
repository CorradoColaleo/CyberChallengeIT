#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
fin = open("2025-keyboard_keyboard-2_1738076117.txt", "r")  # Input file provided by the platform
fout = open("outputMio.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
#fin = sys.stdin  # Input
#fout = sys.stdout  # Output


def find_key(L, s):
    # WRITE YOUR CODE HERE
    alfa = set("abcdefghijklmnopqrstuvwxyz")
    lettera = list(alfa - set(s))[0]
    return lettera

N = int(fin.readline().strip())

for _ in range(N):
    L = int(fin.readline().strip())
    s = fin.readline().strip()
    print(find_key(L, s))