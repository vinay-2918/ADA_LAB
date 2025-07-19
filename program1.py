import time
import matplotlib.pyplot as plt
import random

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

sizes = list(range(1000, 10001, 1000))  # Input sizes from 1000 to 10000
times = []

for size in sizes:
    arr = [random.randint(1, size) for _ in range(size)]
    key = -1  # Worst-case: key not in array
    start = time.time()
    linear_search(arr, key)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times, marker='o', color='blue')
plt.title("Linear Search Time Complexity")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()
# This code implements a linear search algorithm and measures its time complexity for different input sizes.
# It generates random arrays of increasing sizes and searches for a key that is not present in the array.