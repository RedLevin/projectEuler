def primes(n):
    primes = []
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

primesList = primes(1000000)

print(primesList)

def primeFactors(n, primes):
    count = 0
    for p in primes:
        if(int(n/2)+2<p):
            break
        if(n%p==0):
            count += 1
    return count

consecutive = 0

for i in range(10000000):
    if(i%1000000==0):
        print(i)    
    count = primeFactors(i, primesList)
    if(count==4):
        consecutive += 1
    else:
        consecutive = 0
    if(consecutive==4):
        print(i-3)
        print("⭐⭐⭐⭐⭐")
        break