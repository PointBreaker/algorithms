def merge(a, b, cnt):
    # merge two sorted list
    if len(a) == 0:
        return b, cnt
    if len(b) == 0:
        return a, cnt
    if a[0] < b[0]:
        res, cnt = merge(a[1:], b, cnt)
        return [a[0]] + res, cnt
    if a[0] > b[0]:
        res, cnt = merge(a, b[1:], cnt + len(a))
        return [b[0]] + res, cnt
    
def mergesort(nums):
    l = len(nums)
    if l == 0 or l == 1:
        return nums, 0
    mid = l >> 1
    left, cl = mergesort(nums[:mid])
    right, cr = mergesort(nums[mid:])
    nums, res = merge(left, right, 0)
    return nums, cl + cr + res

def counting_inversions(nums):
    l = len(nums)
    if l == 0 or l == 1:
        return nums, 0
    mid = l >> 1
    left, cl = counting_inversions(nums[:mid])
    right, cr = counting_inversions(nums[mid:])
    c = []
    res = 0
    while len(left) != 0 or len(right) != 0:
        if len(left) == 0:
            c += right
            right = []
        elif len(right) == 0:
            c += left
            left = []
        elif left[0] < right[0]:
            c.append(left[0])
            left = left[1:]
        else:
            c.append(right[0])
            right = right[1:]
            res += len(left)
    return c, cl + cr + res
    

if __name__ == "__main__":
    nums = [1, 5, 4, 6, 2, 3, 7, 8,-1]
    print(mergesort(nums))
    print(counting_inversions(nums))
    nums = [1, 3, 2, -1, 6, 8, 7, 9, -2]
    print(mergesort(nums))
    print(counting_inversions(nums))
    nums = [2, 1]
    print(mergesort(nums))
    print(counting_inversions(nums))
    nums = [2, 1, 3]
    print(mergesort(nums))
    print(counting_inversions(nums))
    nums = [4, 2, 1, 3]
    print(mergesort(nums))
    print(counting_inversions(nums))