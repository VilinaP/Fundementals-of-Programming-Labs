primes = [2, 3, 5, 7, 13]

for p in primes:
    perfectNum= (2 ** (p - 1)) * (2 ** p - 1)
    print(perfectNum)
