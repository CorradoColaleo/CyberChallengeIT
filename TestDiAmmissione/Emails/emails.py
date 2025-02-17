#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
fin = open("2025-emails_emails-3_1738081427.txt", "r")  # Input file provided by the platform
fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
#fin = sys.stdin  # Input
#fout = sys.stdout  # Output

def find_sum_of_times(N, M, t, f, emails):
    total_time = 0

    for email_time in emails:
        current_time = email_time

        for i in range(N):
            if current_time % t[i] != 0:
                current_time += t[i] - (current_time % t[i])
            current_time += f[i]

        total_time += current_time

    return total_time

N, M = map(int, fin.readline().strip().split())
t = list(map(int, fin.readline().strip().split()))
f = list(map(int, fin.readline().strip().split()))
emails = list(map(int, fin.readline().strip().split()))

fout.write(str(find_sum_of_times(N, M, t, f, emails)) + "\n")
print(find_sum_of_times(N, M, t, f, emails))