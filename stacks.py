class Stack:
    def __init__(self, amount):
        """
        Initializes a stack with a specified amount of capacity.

        Parameters:
            amount (int): The maximum number of items the stack can hold.
        """
        self.items = [None] * amount  # Initialize the stack with a list of None values
        self.topPointer = -1  # Initialize the top pointer to -1 (empty stack)

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Parameters:
            item: The item to be added to the stack.
        """
        self.items[self.topPointer + 1] = item  # Insert the item at the next available position
        self.topPointer += 1  # Move the top pointer up one position
    
    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Returns:
            Any: The item removed from the top of the stack, or "stack empty" if the stack is empty.
        """
        if self.topPointer == -1:  # If the stack is empty
            return "stack empty"
        else:
            return self.items.pop(self.topPointer)  # Remove and return the top item from the stack

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            Any: The item at the top of the stack, or "Stack empty" if the stack is empty.
        """
        if self.topPointer == -1:  # If the stack is empty
            return "Stack empty"
        else:
            return self.items[self.topPointer]  # Return the top item from the stack

## Testing
myStack = Stack(12)  # Creating an instance of the Stack class with capacity of 12

myStack.push(2)
myStack.push(4)
myStack.push(6)
myStack.push(8)
print(myStack.peek())  # Output: 8 (the top element of the stack)
