# Define a 2D array (list of lists)
array2d = [[1, 2],  # Row 0
            [3, 4]]  # Row 1

# Accessing elements in a 2D array
element_00 = array2d[0][0]  # Accesses the element at row 0, column 0 (value: 1)
element_11 = array2d[1][1]  # Accesses the element at row 1, column 1 (value: 4)

# Modifying elements in a 2D array
array2d[0][1] = 5  # Modifies the element at row 0, column 1 to 5

# Iterating through a 2D array
for row in array2d:
    for element in row:
        print(element, end=' ')  # Prints each element separated by a space
    print()  # Prints a newline after each row
