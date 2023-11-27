def modular_fft(p, roots, modulu=5):
    n = len(p)
    if n == 1:
        return p
    mid = n >> 1
    y_even = modular_fft(p[0:n:2], roots[0:n:2])
    y_odd = modular_fft(p[1:n:2], roots[0:n:2])
    y = [0] * n
    for i in range(mid):
        y[i] = (y_even[i] + roots[i] * y_odd[i]) % modulu
        y[i+mid] = (y_even[i] + roots[i+mid] * y_odd[i]) % modulu
    return y

def modular_ifft(val, roots, modulu=5):
    res = modular_fft(val, roots)
    res = [4 * i % modulu for i in res]
    return res
    
if __name__ == "__main__":
    a = [0, 2, 3, 0]
    print(modular_fft(a, [1, 2, 4, 3]))
    val = [0, 1, 4, 0]
    print(modular_ifft(val, [1, 3, 4, 2]))
    print(modular_ifft([1, 0], [1, 4]))
