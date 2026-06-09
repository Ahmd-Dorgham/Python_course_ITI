def b_sort(l):
    size = len(l)
    for i in range(size):
        for j in range(size - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l

nums = [64, 34, 25, 12, 22, 11, 90]
print("Array after sort:", b_sort(nums))