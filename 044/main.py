def pentagonNumber(n):
    return int((n*(3*n-1))/2)

def isPentagon(n, pentagonNumbers):
    return n in pentagonNumbers

pentagonNumbers = []

pentagonPairs = []

for i in range(1, 1000000):
    pentagonNumbers.append(pentagonNumber(i))

print(pentagonNumbers[-1])

#1200
k = 2100
for i in range(k, k+300):
    if(i%10==0):
        print(i)
    iP = pentagonNumbers[i]
    for j in range(5000):
        if(i < j):
            break
        jP = pentagonNumbers[j]
        if(isPentagon(iP-jP, pentagonNumbers)):
            print(iP, jP)
            if(isPentagon(iP+jP, pentagonNumbers)):
                print(iP, jP)
                print("special")
                print("special")
                print("⭐ ⭐ ⭐ ⭐ ⭐ ")
                pentagonPairs.append(iP, jP)

print(pentagonPairs)