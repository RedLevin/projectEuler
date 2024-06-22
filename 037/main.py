truncatable_primes = []

def isTruncatable(prime, primes):
    str_prime = str(prime)
    if len(str_prime) == 1:
        return False
    for i in range(1, len(str_prime)):
        if int(str_prime[i:]) not in primes:
            return False
        if int(str_prime[:i]) not in primes:
            return False
    return True

def primes(number):
    primes = []
    for i in range(2, number+1):
        isPrime = True
        for prime in primes:
            if (i**0.5+2) < prime:
                break
            if i%prime == 0:
                isPrime = False
                break
        if isPrime: 
            primes.append(i)
            if(isTruncatable(i, primes)):
                truncatable_primes.append(i)
                print(truncatable_primes)
                if len(truncatable_primes) == 11:
                    sum = 0
                    for t_p in truncatable_primes:
                        sum += t_p
                    print(f"sum for all t p s {sum}")

primes(1000000)

