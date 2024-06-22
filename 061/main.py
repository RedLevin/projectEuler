def trianlgeNumber(n):
    return int((n*(n+1))/2)

def squareNumber(n):
    return n**2

def pentagonalNumber(n):
    return int((n*(3*n-1))/2)

def hexagonalNumber(n):
    return n*(2*n-1)

def heptagonalNumber(n):
    return int((n*(5*n-3))/2)

def octagonalNumber(n):
    return n*(3*n-2)

def polgonyalNumbers(type):
    polygonalNumbers = []
    pN = 1
    n = 1
    while (pN < 10000):
        if(pN >= 1000):
            polygonalNumbers.append(pN)
        n += 1
        pN = type(n)
    return polygonalNumbers

trianlgeNumbers = polgonyalNumbers(trianlgeNumber)
squareNumbers = polgonyalNumbers(squareNumber)
pentagonalNumbers = polgonyalNumbers(pentagonalNumber)
hexagonalNumbers = polgonyalNumbers(hexagonalNumber)
heptagonalNumbers = polgonyalNumbers(heptagonalNumber)
octagonalNumbers = polgonyalNumbers(octagonalNumber)

polgonyalNumbersList = [trianlgeNumbers, squareNumbers, pentagonalNumbers, hexagonalNumbers, heptagonalNumbers, octagonalNumbers]
perm = ["0", "1", "2", "3", "4", "5"]

def permutations(list):
    if(len(list) == 1):
        return list
    perms = []
    for e in list:
        list2 = list.copy()
        list2.remove(e)
        for e2 in permutations(list2):
            perms.append(e + e2)
    return perms

perms = permutations(perm)

def pe061(polgonyalNumbersList):
    for a in polgonyalNumbersList[0]:
        aStr = str(a)
        aStart = aStr[:2]
        aEnd = aStr[-2:]
        for b in polgonyalNumbersList[1]:
            bStr = str(b)
            bStart = bStr[:2]
            if(not aEnd == bStart):
                continue
            bEnd = bStr[-2:]
            for c in polgonyalNumbersList[2]:
                cStr = str(c)
                cStart = cStr[:2]
                if(not bEnd == cStart):
                    continue
                cEnd = cStr[-2:]
                for d in polgonyalNumbersList[3]:
                    dStr = str(d)
                    dStart = dStr[:2]
                    if(not cEnd == dStart):
                        continue
                    dEnd = dStr[-2:]
                    for e in polgonyalNumbersList[4]:
                        eStr = str(e)
                        eStart = eStr[:2]
                        if(not dEnd == eStart):
                            continue
                        eEnd = eStr[-2:]
                        for f in polgonyalNumbersList[5]:
                            fStr = str(f)
                            fStart = fStr[:2]
                            if(not eEnd == fStart):
                                continue
                            fEnd = fStr[-2:]
                            if(fEnd == aStart):
                                print(a, b, c, d, e, f)
                                print(a + b + c + d + e + f)
                                print("⭐⭐⭐⭐⭐")

for p in perms:
    polyPerms = []
    for w in p:
       polyPerms.append(polgonyalNumbersList[int(w)])
    pe061(polyPerms)
