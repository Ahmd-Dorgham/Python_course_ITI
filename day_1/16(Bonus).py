def diag_diff(matrix):
    sum1 = 0
    sum2 = 0
    size = len(matrix)
    
    for r in range(size):
        sum1 = sum1 + matrix[r][r]
        sum2 = sum2 + matrix[r][size - 1 - r]
        
    if sum1 > sum2:
        return sum1 - sum2
    else:
        return sum2 - sum1

m = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print("Difference is", diag_diff(m))