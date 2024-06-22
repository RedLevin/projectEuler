number = 10000000

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

"""
def isPandigital(n):
    str_n = str(n)
    for i in range(10):
        if str(i) not in str_n:
            return False
    return True
"""

primesList = primes(int(number**0.5)+2)

#maxPandigitalPrime = 0

#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
def createPandigitals(array):
    if(len(array) == 1):
        return array
    pandigitals = []
    for a in array:
        array2 = array.copy()
        array2.remove(a)
        for b in createPandigitals(array2):
            pandigitals.append(a+b)
    return pandigitals

digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]

def truncatable(array):
    truncatables = [array]
    for i in range(1, len(array)):
        truncatables.append(array[i:])
    return truncatables

tt = truncatable(digits)

#print(f"is pirme {isPrime(98745623, primesList)}")

pandigitials = []


for t in tt:
    pandigitials.extend(createPandigitals(t))

pp = []
maxPP = 0

for str_p in pandigitials:
    p = int(str_p)
    if(isPrime(p, primesList)):
        pp.append(p)
        if(p > maxPP):
            maxPP = p

print(maxPP)

