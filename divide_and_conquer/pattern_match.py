from poly_multiply import poly_multiply
def naive_match(sequence, pattern, k=0):
    res = []
    n = len(pattern)
    m = len(sequence)
    goal = n - k
    for i in range(m - n + 1):
        t = 0
        for j in range(n):
            if sequence[i + j] == pattern[j]:
                t += 1
        if t >= goal:
            res.append(i)
    return res

def fft_match(sequence, pattern, k=0):
    psequence = []
    ppattern = []
    n = len(pattern)
    for i in sequence:
        if i == "0":
            psequence.append(-1)
        if i == "1":
            psequence.append(1)
    for i in pattern[::-1]:
        if i == "0":
            ppattern.append(-1)
        if i == "1":
            ppattern.append(1)
    val = poly_multiply(psequence, ppattern)
    m = len(val)
    val = val[n-1: m-n+1]
    res = []
    for i, v in enumerate(val):
        if v > k:
            res.append(i)
    return res

pattern_match = fft_match
    
if __name__ == "__main__":
    pattern = "0111"
    sequence = "01010110111"
    print(pattern_match(sequence, pattern, k=1))