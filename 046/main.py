def primes(n):
    primes = []
    pandigital = 0
    for i in range(2, n+1):
        isPrime = True
        for p in primes:
            if(p > (i**0.5+2)):
                break
            if(i%p==0):
                isPrime = False
                break
        if isPrime: 
            primes.append(i)
    return primes

def isPrime(n, primes):
    isPrime = True
    for p in primes:
        if(p > (n**0.5+2)): 
            break
        if(n%p==0):
            isPrime = False
            break
    return isPrime

primesList = (primes(1000000))

def testGoldbach(n, primes):
    for p in primes:
        if(p >= n):
            break
        for i in range(1, int(n/2)):
            if(p+2*i**2==n):
                return False
    return True

for i in range(9, 1000000, 2):
    if((i+1)%100==0):
        print(i)
    if(i in primesList):
        continue    
    if(testGoldbach(i, primesList)):
        print(i)
        print("⭐⭐⭐⭐⭐")
        break