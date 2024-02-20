List = [1, 3, 4, 7, 6, 4]  # Define a list of integers

def linear_search(arr: list, query: int) -> int:
    """
    Perform linear search to find the index of the query element in the list.

    Parameters:
        arr (list): The list to search in.
        query (int): The element to search for.

    Returns:
        int: The index of the query element if found, otherwise -1.
    """
    for i in range(len(arr)):  # Iterate through each element in the list
        if arr[i] == query:  # If the current element matches the query
            return i  # Return the index of the query element
    return -1  # Return -1 if the query element is not found

print(linear_search(List, 6))  # Perform linear search for element 6 in the list
