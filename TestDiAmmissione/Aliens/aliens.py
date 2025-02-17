#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
fin = open("2025-aliens_aliens-3_1738077175.txt", "r")  # Input file provided by the platform
fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
#fin = sys.stdin  # Input
#fout = sys.stdout  # Output

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ALPHABET_LEN = len(ALPHABET)

def execute_code(N, code):
    result = []

    for operation in code:
        parts = operation.split()
        cmd = parts[0]

        if cmd == "add":
            result.append(parts[1])

        elif cmd == "del":
            if result:
                result.pop()

        elif cmd == "swap":
            a, b = parts[1], parts[2]
            result = [b if c == a else a if c == b else c for c in result]

        elif cmd == "rot":
            x = int(parts[1])
            result = [
                ALPHABET[(ALPHABET.index(c) + x) % ALPHABET_LEN] if c in ALPHABET else c
                for c in result
            ]

    return "".join(result)

N = int(fin.readline().strip())
code = []

for _ in range(N):
    s = fin.readline().strip()
    code.append(s)

output = execute_code(N, code)
fout.write(output + "\n")
