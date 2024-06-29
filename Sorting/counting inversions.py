#!/bin/python3

# Complete the countInversions function below.
def countInversions(arr):
    if len(arr) < 2:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    inversions = countInversions(left) + countInversions(right)
    
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inversions += len(left) - i
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return inversions

#The second line contains space-separated integers.
with open("IntegerArray.txt", "r") as f:
    lines = [int(line.strip()) for line in f]

result = countInversions(lines)

print(result)
