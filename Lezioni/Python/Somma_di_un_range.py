def sum_range(inizio,fine):
    if inizio > fine:
        inizio,fine=fine,inizio
    somma = 0
    for i in range(inizio,fine+1):
        somma += i
    return somma

def main():
    print(sum_range(1,10))

main()