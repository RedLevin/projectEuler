def pq(p, q):
    a = -(p/2)
    b = ((p/2)**2-q)**0.5
    x1 = a + b
    return x1

def isPentagonal(n):
    p = -1/3
    q = (-n*2)/3
    x1 = pq(p, q)
    if(x1%1==0):
        return True
    else:
        return False
    
def isHexagonal(n):
    p = -1/2
    q = -n/2
    x1 = pq(p, q)
    if(x1%1==0):
        return True
    else:
        return False
    
def triangleNumber(n):
    return (n*(n+1))/2

for i in range(1, 1000000):
    t = triangleNumber(i)
    if(isPentagonal(t) and isHexagonal(t)):
        print("⭐⭐⭐⭐⭐")
        print(i)
        print(t)
        print("⭐⭐⭐⭐⭐")
        print("\n")