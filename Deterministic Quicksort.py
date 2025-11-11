# Adopting deterministic Quicksort algorithm where the last element of the array is chosen as a pivot, the array is recursively divided into smaller subarrays and the results of the sorted data are recombined to form the final ordered list.

# Defining a function to implement deterministic quicksort
def quicksort(arr):
    # Checking if the array has 1 or no elements (base case)
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the last element as the pivot
        pivot = arr[-1]

        # Dividing the array into two parts: elements less than or equal to pivot and greater than pivot
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        # Recursively sorting both parts and combining them
        return quicksort(left) + [pivot] + quicksort(right)


# Taking user input for array elements
user_input = input("Enter numbers separated by spaces: ")

# Converting the input string into a list of integers
arr = list(map(int, user_input.split()))

# Calling the quicksort function to sort the array
sorted_arr = quicksort(arr)

# Printing the sorted result
print("Sorted array using Deterministic Quicksort:", sorted_arr)
