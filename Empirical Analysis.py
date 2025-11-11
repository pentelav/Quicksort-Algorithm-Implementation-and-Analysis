# Empirical analysis of deterministic and randomized Quicksort algorithm.
# Run time measurement with different input sizes and distributions: random, sorted and reverse-sorted.
# Comparison of impacts on sorting of randomization.

import time            # Importing time module for measuring execution time
import numpy as np      # Importing numpy for generating test data
import random           # Importing random module for random pivot selection
import sys              # Importing sys module for modifying recursion limits

# Increasing recursion limit to safely handle deep recursive calls for large arrays
sys.setrecursionlimit(30000)


# Deterministic Quicksort
def quicksort(arr):
    # Checking if array length is 1 or less
    if len(arr) <= 1:
        return arr
    # Choosing middle element as pivot to improve balance
    pivot = arr[len(arr) // 2]
    # Creating left subarray with elements less than pivot
    left = [x for x in arr if x < pivot]
    # Creating middle subarray with elements equal to pivot
    middle = [x for x in arr if x == pivot]
    # Creating right subarray with elements greater than pivot
    right = [x for x in arr if x > pivot]
    # Recursively sorting and combining results
    return quicksort(left) + middle + quicksort(right)


# Randomized Quicksort
def randomized_quicksort(arr):
    # Checking if array has one or no elements
    if len(arr) <= 1:
        return arr
    # Selecting a random pivot element from array
    pivot = random.choice(arr)
    # Creating left subarray with elements less than pivot
    left = [x for x in arr if x < pivot]
    # Creating middle subarray with elements equal to pivot
    middle = [x for x in arr if x == pivot]
    # Creating right subarray with elements greater than pivot
    right = [x for x in arr if x > pivot]
    # Recursively sorting and returning combined output
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


# Time Measurement Function
def measure_time(sort_func, arr):
    # Recording start time
    start_time = time.time()
    # Performing sorting on a copy of the array
    sort_func(arr.copy())
    # Calculating and returning total elapsed time
    return time.time() - start_time


# Defining Input Sizes and Distributions
# Defining input sizes for performance measurement
sizes = [1000, 5000, 10000, 20000]

# Defining input distributions for testing algorithm behavior under different conditions
distributions = {
    "Random": lambda n: np.random.randint(0, 100000, n).tolist(),  # Generating random numbers
    "Sorted": lambda n: list(range(n)),                             # Generating already sorted sequence
    "Reverse": lambda n: list(range(n, 0, -1))                      # Generating reverse-sorted sequence
}


# Performing Empirical Analysis
# Iterating through each data distribution type
for dist_name, gen in distributions.items():
    # Printing current distribution being analyzed
    print(f"\nAnalyzing Distribution: {dist_name}")
    # Iterating through each input size
    for n in sizes:
        # Generating array of specified size and distribution
        arr = gen(n)
        # Measuring run time of deterministic Quicksort
        det_time = measure_time(quicksort, arr)
        # Measuring run time of randomized Quicksort
        rand_time = measure_time(randomized_quicksort, arr)
        # Displaying comparative run times for both algorithms
        print(f"Array Size {n}: Deterministic={det_time:.5f}s, Randomized={rand_time:.5f}s")
