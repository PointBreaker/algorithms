import math
def naive_approach(n):
    n = int(n)
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return naive_approach(n >> 1) + naive_approach(n % 2)
    
def add_binary(a, b):
    if not (a and b):
        return a or b or '0'
    out = ''
    carry = '0'
    for d1, d2 in zip(a[::-1], b[::-1]):
        # case 1: 0 + 0
        if d1 == '0' and d2 == '0':
            out += carry
            carry = '0'
        # case 2: 1 + 1
        elif d1 == '1' and d2 == '1':
            out += carry
            carry = '1'
        # case 3: 0 + 1 or 1 + 0
        else:
            if carry == '0':
                out += '1'
            else:
                out += '0'

    remaining_bits = a[:-len(out)] or b[:-len(out)]
    if carry == '0':
        return remaining_bits + out[::-1]
    return (add_binary(remaining_bits, carry) + out[::-1]).lstrip('0') or '0'

def sub_binary(a, b):
    if not b:
        return a or '0'
    assert int(a) >= int(b), 'a must be at least as large as b'
    out = ''
    for i in range(1, 1 + min(len(a), len(b))):
        # case 1: 0 - 0 or 1 - 1
        if a[-i] == b[-i]:
            out += '0'
        # case 2: 1 - 0
        elif a[-i] == '1' and b[-i] == '0':
            out += '1'
        # case 3: 0 - 1
        elif a[-i] == '0' and b[-i] == '1':
            out += '1'
            a = sub_binary(a, '1' + '0'*(i))

    remaining_bits = a[:-len(out)]
    return (remaining_bits + out[::-1]).lstrip('0') or '0'

def mul_binary(a, b):
    n = max(len(a), len(b))
    x = '0'*(n-len(a)) + a
    y = '0'*(n-len(b)) + b
    
    if n == 1 and x == y == '1':
        return '1'
    elif n == 1:
        return '0'
    
    xlo = x[n//2:]
    xhi = x[:n//2]
    ylo = y[n//2:]
    yhi = y[:n//2]
    
    A = mul_binary(xhi, yhi)
    B = mul_binary(xlo, ylo)
    E = mul_binary(add_binary(xlo, xhi), add_binary(ylo, yhi))
    
    result = A + '0'*(2*len(xlo))
    result = add_binary(result, sub_binary(E, add_binary(A, B))+'0'*len(xlo))
    result = add_binary(result, B)
    
    return result.lstrip('0') or '0'

def divideAndConquer(n):
    if n <= 10:
        return naive_approach(n)
    length = math.log10(n) + 1
    mid = length // 2
    x_left = n // (10 ** mid)
    x_right = n % (x_left * (10 ** mid))
    high = divideAndConquer(x_left)
    tails = divideAndConquer(10 ** mid)
    low = divideAndConquer(x_right)
    return add_binary(mul_binary(high, tails), low)

decimal_to_binary = divideAndConquer

if __name__ == "__main__":
    print(decimal_to_binary(145))