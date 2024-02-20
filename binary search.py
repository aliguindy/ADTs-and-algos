def binary_search(arr: list , query: int) -> int:
    bottom = 0  # Initialize the bottom index of the search range
    top = len(arr)  # Initialize the top index of the search range
    mid = (top + bottom)//2  # Calculate the mid index of the search range
    found = False  # Initialize the flag to track if the element is found

    while not found:
        mid = (top + bottom)//2  # Calculate the mid index again in each iteration
        
        if query > arr[mid]:  # If the query is greater than the element at mid index
            found = False  # Set found flag to False
            bottom = mid + 1  # Update the bottom index for the new search range
        elif query < arr[mid]:  # If the query is less than the element at mid index
            found = False  # Set found flag to False
            top = mid - 1  # Update the top index for the new search range
        elif query == arr[mid]:  # If the query matches the element at mid index
            return mid  # Return the index of the element
    return -1  # Return -1 if the element is not found

List = [1, 3, 4, 6, 7]  # Define a sorted list
print(binary_search(List, 6))  # Perform binary search for element 6 in the list
