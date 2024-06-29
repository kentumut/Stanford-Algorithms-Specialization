def quicksort_in_place(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_in_place(arr, low, pivot_index - 1)
        quicksort_in_place(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Use the first element as the pivot
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Read the file and create the array
with open('QuickSort.txt', 'r') as file:
    liste = [int(line.strip()) for line in file]

# Initialize comparison count
# Perform the quicksort
quicksort_in_place(liste, 0, len(liste) - 1)

# Output the total number of comparisons
print(liste)
