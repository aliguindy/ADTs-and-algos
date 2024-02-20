import random  # Importing the random module to generate random numbers

# Generate a list of unique random integers between 0 and 100
myList = []
for i in range(8):
    a = random.randint(0, 100)
    myList.append(a)
myList = list(set(myList))  # Remove duplicates by converting to set and back to list

print(f"unsorted list: {myList}")  # Print the unsorted list

def bubblesort(arr):
    """
    Sorts a list using the bubble sort algorithm.

    Parameters:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    size = len(arr)
    swapped = True
    pass_number = 0

    while swapped and pass_number < size - 1:
        swapped = False
        for i in range(size - pass_number - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap elements if they are out of order
                swapped = True
        pass_number += 1
    return arr

print(bubblesort(myList))  # Print the sorted list obtained using bubble sort
