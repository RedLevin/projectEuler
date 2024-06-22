f = open('primesList.txt', 'r')
primesString = f.read()
primesList = primesString.split(',')
primesList = list(map(int, primesList))
lengthPrimesList = len(primesList)

def binarySearch(list, element):
    low, high = 0, len(list)
    while(low != high):        
        mid = int((high-low)/2+low)
        if(element > list[mid]):
            low =  mid+1
        elif(element < list[mid]):
            high = mid
        else:
            return True
    return False

def crossfootModulusThree(n):
    crossfoot = 0
    for s in str(n):
        crossfoot += int(s)
    return crossfoot%3

def concatNumbers(n1, n2):
    return int(str(n1)+str(n2))

def testPrimePairs(oldPrimes, newPrime):
    for oldPrime in oldPrimes:
        if(not binarySearch(primesList, concatNumbers(oldPrime, newPrime))):
            return False
        if(not binarySearch(primesList, concatNumbers(newPrime, oldPrime))):
            return False
    if(len(oldPrimes)==3):
        print(oldPrimes, newPrime, "🔥")
    return True

for a in range(lengthPrimesList):
    aPrime = primesList[a]
    aModulusThree = crossfootModulusThree(aPrime)
    modulusType = 0
    if(aModulusThree == 1):
        modulusType = 2
    if(aModulusThree == 2):
        modulusType = 1
    for b in range(lengthPrimesList):
        if(a<=b):
            break
        bPrime = primesList[b]
        bModulusThree = crossfootModulusThree(bPrime)
        if(bModulusThree == modulusType):
            continue
        if(not testPrimePairs([aPrime], bPrime)):
            continue
        for c in range(lengthPrimesList):
            if(b<=c):
                break
            cPrime = primesList[c]
            cModulusThree = crossfootModulusThree(cPrime)
            if(cModulusThree == modulusType):
                continue
            if(not testPrimePairs([aPrime, bPrime], cPrime)):
                continue
            for d in range(lengthPrimesList):
                if(c<=d):
                    break
                dPrime = primesList[d]
                dModulusThree = crossfootModulusThree(dPrime)
                if(dModulusThree == modulusType):
                    continue
                if(not testPrimePairs([aPrime, bPrime, cPrime], dPrime)):
                    continue
                for e in range(lengthPrimesList):
                    if(d<=e):
                        break
                    ePrime = primesList[e]
                    eModulusThree = crossfootModulusThree(ePrime)
                    if(bModulusThree == modulusType):
                        continue
                    if(testPrimePairs([aPrime, bPrime, cPrime, dPrime], ePrime)):
                        print("⭐ ⭐ ⭐ ⭐ ⭐")
                        print(aPrime, bPrime, cPrime, dPrime, ePrime)
                        print(aPrime + bPrime + cPrime + dPrime + ePrime)