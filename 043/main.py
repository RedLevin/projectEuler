def createPandigitals(array, n=0):
    if(len(array) == 1):
        return array
    pandigitals = []
    for a in array:
        if(n==0 and a == "0"): 
            continue
        array2 = array.copy()
        array2.remove(a)
        for b in createPandigitals(array2, n+1):
            pandigitals.append(a+b)
    return pandigitals

digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]

pandigitals = createPandigitals(digits)

weirdNumbers = []
weirdNumberTotal = 0

for p in pandigitals:
    if(int(p[1:4])%2==0):
        if(int(p[2:5])%3==0):
            if(int(p[3:6])%5==0):
                if(int(p[4:7])%7==0):
                    if(int(p[5:8])%11==0):
                        if(int(p[6:9])%13==0):
                            if(int(p[7:10])%17==0):
                                weirdNumbers.append(int(p))
                                weirdNumberTotal += int(p)

print(weirdNumberTotal)

                

