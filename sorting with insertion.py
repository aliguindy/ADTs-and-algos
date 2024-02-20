import random  # Importing the random module to generate random numbers

# Generate a list of unique random integers between 0 and 100
myList = []
for i in range(8):
    a = random.randint(0, 100)
    myList.append(a)
myList = list(set(myList))  # Remove duplicates by converting to set and back to list

print(f"unsorted list: {myList}")  # Print the unsorted list

## Insertion Sort Algorithm ##
def insertion_sort(arr):
    """
    Sorts a list using the insertion sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]  # Select the current element to be inserted into the sorted subarray
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key into its correct position in the sorted subarray
    return arr

insertion_sort(myList)  # Sort the list using insertion sort (in-place)
print("Sorted array is:", insertion_sort(myList))  # Print the sorted list
