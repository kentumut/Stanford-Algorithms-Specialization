def quicksort_in_place(arr, low, high, comparison_count):
    if low < high:
        pivot_index, comparisons = partition(arr, low, high)
        comparison_count[0] += comparisons
        quicksort_in_place(arr, low, pivot_index - 1, comparison_count)
        quicksort_in_place(arr, pivot_index + 1, high, comparison_count)

def partition(arr, low, high):
    pivot = arr[low]  # Use the first element as the pivot
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    comparisons = (high - low)  # Number of comparisons is the size of the subarray minus one
    return i - 1, comparisons

# Read the file and create the array
with open('QuickSort.txt', 'r') as file:
    liste = [int(line.strip()) for line in file]

# Initialize comparison count
comparison_count = [0]

# Perform the quicksort
quicksort_in_place(liste, 0, len(liste) - 1, comparison_count)

# Output the total number of comparisons
print(comparison_count[0])
