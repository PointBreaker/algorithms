def merge(a, b):
    # merge two sorted list
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    if a[0] > b[0]:
        return [b[0]] + merge(a, b[1:])
    
def mergesort(nums):
    l = len(nums)
    if l == 0 or l == 1:
        return nums
    mid = l >> 1
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right)
    

if __name__ == "__main__":
    l = [1, 5, 6, 7]
    r = [2, 3, 4, 8]
    print(merge(l, r))
    nums = [1, 5, 4, 6, 2, 3, 7, 8]
    print(mergesort(nums))