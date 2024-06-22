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

def createPermutations(array, perms=0, counter=1):
    if(len(array) == 1):
        return array
    if(perms==counter):
        return array
    permutations = []
    for a in array:
        array2 = array.copy()
        array2.remove(a)
        for b in createPermutations(array2, perms, counter+1):
            permutations.append(a+b)
    return permutations

prime = 0

while(prime == 0):
    for p in primesList:
        print(p)
        digits = []
        pLength = len(str(p))
        for i in range(pLength):
            digits.append(str(i))
        permsArray = []
        for i in range(1, pLength):            
            permsArray.extend(createPermutations(digits, i))
        for perms in permsArray:
            primeList = []
            primeCounter = 0
            pString = str(p)
            pList = list(pString)
            for i in range(10):
                zeroCase = False
                goodIdea = True
                for j in range(len(perms)):
                    if(pString[int(perms[j])] != pString[int(perms[0])]):
                        goodIdea = False
                        break
                if(goodIdea == False):
                    break
                for perm in perms:                    
                    if(perm == "0" and i == 0):
                        zeroCase = True
                    pList[int(perm)] = str(i)
                    pString = "".join(pList)
                if(int(pString) in primesList and not zeroCase):
                    primeCounter += 1
                    primeList.append(pString)
            if(primeCounter > 6):
                print(p)    
                print(perms)
                print(primeList)
                print(primeCounter)
                print("\n")
                if(primeCounter > 7):
                    print("⭐ ⭐ ⭐ ⭐ ⭐")
                    prime = p