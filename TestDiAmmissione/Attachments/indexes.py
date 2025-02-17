import sys
import math

def precompute_triples(M):
    triples = []
    for x in range(1, M+1):
        for y in range(x, M+1): 
            product = x*y
            z = int(math.isqrt(product))
            if z*z == product and z <= M:
                triples.append((x, y, z))
                if y != x:
                    triples.append((y, x, z))
    return triples

def check_subarray_valid(freq, triples):
    for (x, y, z) in triples:
        if x == y == z:
            if freq[x] >= 3:
                return True
        elif x == y != z:
            if freq[x] >= 2 and freq[z] >= 1:
                return True
        elif x != y == z:
            if freq[y] >= 2 and freq[x] >= 1:
                return True
        elif x != y and y != z and z != x:
            if freq[x] >= 1 and freq[y] >= 1 and freq[z] >= 1:
                return True
    return False

def count_intervals_bruteforce(N, a):
    M = max(a) if a else 0
    if M == 0:
        return 0
    
    triple_list = precompute_triples(M)
    prefixFreq = [[0]*(N+1) for _ in range(M+1)]
    for i in range(N):
        val = a[i]
        for v in range(1, M+1):
            prefixFreq[v][i+1] = prefixFreq[v][i]
        prefixFreq[val][i+1] += 1
    
    count_good = 0
    for l in range(N):
        for r in range(l, N):
            freq_sub = [0]*(M+1)
            for v in range(1, M+1):
                freq_sub[v] = prefixFreq[v][r+1] - prefixFreq[v][l]
            if check_subarray_valid(freq_sub, triple_list):
                count_good += 1
    return count_good

def count_intervals(N, a):
    return count_intervals_bruteforce(N, a)

def solve():
    import sys
    
    fin = open("2025-indexes_indexes-2_1738083214.txt", "r")
    fout = open("output.txt", "w")
    
    T = int(fin.readline().strip())
    for _ in range(T):
        N = int(fin.readline().strip())
        a = list(map(int, fin.readline().strip().split()))
        answer = count_intervals(N, a)
        fout.write(str(answer) + "\n")
    
    fout.flush()

if __name__ == "__main__":
    solve()