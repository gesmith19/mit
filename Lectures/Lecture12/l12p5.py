def genPrimes():
    '''Write a generator, genPrimes, that returns the sequence of prime 
    numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...'''
    n = 2
    primes = []
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1