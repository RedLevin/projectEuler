def primes(number):
    primes = [2, 3]
    three = 0
    for i in range(5, number+1, 2):
        three += 1
        if(three == 3):
            three = 0
            continue
        isPrime = True
        for prime in primes:
            if (i**0.5+2) < prime:
                break
            if i%prime == 0:
                isPrime = False
                break
        if isPrime: primes.append(i)
    return primes

primesList = primes(100000000)

with open('primesList.txt', 'w') as f:
    f.write(','.join(str(prime) for prime in primesList))