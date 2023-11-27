def kth_smallest(a, b, k):
    if k == 0:
        return min(a[0], b[0])
    if k == 1:
        return max(a[0], b[0])
    mida = len(a) >> 1
    midb = len(b) >> 1
    if (a[mida] < b[midb]):
        return kth_smallest(a[mida:], b[:midb], k - mida - 1)
    else:
        return kth_smallest(a[:mida], b[midb:], k - midb - 1)
    
if __name__ == "__main__":
    a = [1, 3, 5]
    b = [2, 4, 6]
    print(kth_smallest(a, b, 3))
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8]
    print(kth_smallest(a, b, 4))

