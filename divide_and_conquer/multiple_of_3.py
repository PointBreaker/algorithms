def multiples_of_3(A):
    odds = [0] * 3
    evens = [0] * 3
    if len(A) == 0:
        return odds, evens
    if len(A) == 1:
        odds[A[0] % 3] += 1
        return odds, evens
    mid = len(A) >> 1
    left_odd, left_even = multiples_of_3(A[:mid])
    right_odd, right_even = multiples_of_3(A[mid:])
    for i in range(3):
        odds[i] += left_odd[i]
        odds[i] += right_odd[i]
        evens[i] += left_even[i]
        evens[i] += right_even[i]
        for j in range(3):
            m = (i + j) % 3
            odds[m] += left_odd[i] * right_even[j]
            odds[m] += left_even[i] * right_odd[j]
            evens[m] += left_odd[i] * right_odd[j]
            evens[m] += left_even[i] * right_even[j]
    return odds, evens
    
if __name__ == "__main__":
    A = [3, 6, 9, 12, 15, 18, 21, 24]
    print(multiples_of_3(A)[0][0])