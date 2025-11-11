# Applying randomized Quicksort algorithm according to which a random element is chosen as a pivot, the array is divided into several subarrays according to the pivot value, and the subarrays are sorted recursively to obtain an efficient list.

import random  # Importing the random module for selecting a random pivot

# Defining a function to implement randomized quicksort
def randomized_quicksort(arr):
    # Checking if the array has 1 or no elements (base case)
    if len(arr) <= 1:
        return arr
    else:
        # Choosing a random index as the pivot
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]

        # Dividing elements into two lists based on the pivot value
        left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        right = [x for i, x in enumerate(arr) if x > pivot]

        # Recursively sorting both parts and combining them
        return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)


# Taking user input for array elements
user_input = input("Enter numbers separated by spaces: ")

# Converting the input string into a list of integers
arr = list(map(int, user_input.split()))

# Calling the randomized quicksort function to sort the array
sorted_arr = randomized_quicksort(arr)

# Printing the sorted result
print("Sorted array using Randomized Quicksort:", sorted_arr)
