from poly_multiply import poly_multiply
def counting_k_inversions(s):
    n = len(s)
    ones = [0] * n
    zeros = [0] * n
    for i, c in enumerate(s):
        if c == "0":
            zeros[i] = 1
        if c == "1":
            ones[n - i - 1] = 1
    product = poly_multiply(zeros, ones)
    n = len(s)
    res = {}
    for i, v in enumerate(product):
        if i > n - 1 and v > 0:
            res[i - n + 1] = v
    return res

if __name__ == "__main__":
    s = "010010"
    print(counting_k_inversions(s))
    s = "100"
    print(counting_k_inversions(s))
    s = "1" 
    print(counting_k_inversions(s))
    s = "0"
    print(counting_k_inversions(s))
    s = "100000"
    print(counting_k_inversions(s))