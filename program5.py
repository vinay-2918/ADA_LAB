def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = list(map(int, input("Enter elements: ").split()))
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
# This code implements the Quick Sort algorithm, which is a popular sorting algorithm.
# The function quick_sort recursively sorts the array by selecting a pivot and partitioning the array into elements less than and greater than the pivot.