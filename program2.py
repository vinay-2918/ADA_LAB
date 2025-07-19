import time
import matplotlib.pyplot as plt
import random

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sizes = list(range(1000, 10001, 1000))  # Input sizes from 1000 to 10000
times = []

for size in sizes:
    arr = sorted(random.sample(range(1, size * 2), size))
    key = -1  # Worst-case: key not in array
    start = time.time()
    binary_search(arr, key)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times, marker='o', color='green')
plt.title("Binary Search Time Complexity")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
# This code implements a binary search algorithm and measures its time complexity for different input sizes.
# It generates sorted arrays of increasing sizes and searches for a key that is not present in the array.