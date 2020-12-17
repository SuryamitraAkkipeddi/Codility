def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)



def solution(A, B):
    count = 0
    for a,b in zip(A, B):
        x = gcd(a,b)
        
        while True:
            d = gcd(x, a)
            if d == 1:
                break
            a /= d

        while True:
            d = gcd(x, b)
            if d == 1:
                break
            b /= d
            
        count  += 1 if a == 1 and b == 1 else 0

    return count