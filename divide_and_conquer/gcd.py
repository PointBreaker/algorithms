def subtract(x, y):
    if y == 0: # gcd(x, 0) = x
        return x
    if x > y:
        return subtract(y, x - y)
    else:
        return subtract(x, y - x)

def euclid(x, y):
    if y == 0: # gcd(x, 0) = x
        return x
    return euclid(y, x % y)

def extend_euclid(x, y):
    if y == 0:
        return (x, 1, 0)
    d, a, b = extend_euclid(y, x % y)
    return (d, b, a - (x // y) * b)
    
    # d = a * y + b * mod(x, y)
    #   = a * y + b * (x - floor(x / y) * y)
    #   = b * x + (a - floor(x / y) * b) * y
    
gcd = extend_euclid

if __name__ == "__main__":
    print(gcd(54, 17))