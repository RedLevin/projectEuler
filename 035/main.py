#returns an array of all numbers that are prime till 'number'
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
        if isPrime: primes.append(i)
    return primes

primes_list = primes(1000000)

print(primes_list)

def circulateNumbers(number):
    circulated_numbers = []
    str_number = str(number)
    for i in range(len(str_number)):
        str_circulated_number = ""
        for j in range(len(str_number)):
            str_circulated_number += str_number[j-i]
        circulated_number = int(str_circulated_number)
        if circulated_number not in circulated_numbers:
            circulated_numbers.append(circulated_number)
    return circulated_numbers

circulated_primes = []

for prime in primes_list:
    circulated = circulateNumbers(prime)
    is_circulated = True
    for c in circulated:
        if c not in primes_list:
            is_circulated = False
    if is_circulated:
        print(prime)
        for c in circulated:
            if c not in circulated_primes:
                circulated_primes.append(c)

print(circulated_primes)

print(len(circulated_primes))