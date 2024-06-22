def diophantineEquation(x, y, D):
    return x**2-D*y**2

def dE2(x, D):
    return ((x**2-1)/D)**0.5

def dE3(y, D):
    return (1+D*(y**2))**0.5

maxX = 0

for D in range(501, 1001):
    print(f"D {D}")
    if(int(D**0.5)==D**0.5):
        continue
    y = 1
    while(True):
        x = dE3(y, D)
        if(x != 1):
            if(int(x) == x):
                if(x > maxX):
                    maxX = x
                    print(f"maxX {maxX}")
                break
        y += 1

print(maxX)
#770394803.0
#501