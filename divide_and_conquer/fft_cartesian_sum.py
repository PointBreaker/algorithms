from poly_multiply import poly_multiply
def cartesian_sum(a, b):
    n = max(a)
    m = max(b)
    la = (n + 1) * [0]
    lb = (m + 1) * [0]
    for i in a:
        la[i] = 1
    for i in b:
        lb[i] = 1
    val = poly_multiply(la, lb)
    res = []
    for i, v in enumerate(val):
        if v != 0:
            res.append(i)
    return res

if __name__ == "__main__":
    print(cartesian_sum([1, 3], [2, 4]))