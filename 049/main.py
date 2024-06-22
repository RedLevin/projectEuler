import time

start = time.time()

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

primesList = primes(10000)

def createPermutations(array):
    if(len(array) == 1):
        return array
    permutations = []
    for a in array:
        array2 = array.copy()
        array2.remove(a)
        for b in createPermutations(array2):
            permutations.append(a+b)
    return permutations

for p in primesList:
    if(len(str(p))!=4):
        continue
    j = 3330    
    n2, n3 = p+j, p+2*j
    iList = [char for char in str(p)]
    permutations = createPermutations(iList)
    if(str(n2) in permutations and str(n3) in permutations):
        print("all permutations")
        print(p)
        if(n2 in primesList and n3 in primesList):
            print("all prime")
            print("⭐⭐⭐⭐⭐")
            print(str(p)+str(n2)+str(n3))

end = time.time()
print(end - start)