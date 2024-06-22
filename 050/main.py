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

maxCount = 0
maxPrime = 0

for i in range(len(primesList)):
    sum = primesList[i]
    count = 1
    while(sum < 1000000 and i+count < len(primesList)):
        sum += primesList[i+count]
        count += 1
        if(count > maxCount):
            if(sum in primesList):
                maxCount = count
                maxPrime = sum

print(maxCount)
print(maxPrime)