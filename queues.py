class Queue:
    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.elements = []  # Initialize the list to store elements in the queue
        self.top = len(self.elements) - 1  # Initialize top pointer at -1 (no elements initially)
        self.bottom = self.top  # Initialize bottom pointer at the same position as top

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.top == self.bottom
    
    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Parameters:
            item: The item to be added to the queue.
        """
        self.elements.append(item)  # Append the item to the list
        self.bottom += 1  # Move the bottom pointer to the new end of the queue

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        Returns:
            Any: The item removed from the front of the queue, or "empty" if the queue is empty.
        """
        if self.is_empty():  # If the queue is empty
            return "empty"
        else:
            dequeued_item = self.elements[self.top + 1]  # Get the item at the front of the queue
            self.top += 1  # Move the top pointer to the next element
            return dequeued_item

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            Any: The item at the front of the queue, or "empty" if the queue is empty.
        """
        if self.is_empty():  # If the queue is empty
            return "empty"
        else:
            return self.elements[self.top + 1]  # Return the item at the front of the queue

# Testing
myQueue = Queue()

myQueue.enqueue(10)
myQueue.enqueue(11)
myQueue.enqueue(12)

print(myQueue.dequeue())  # Output: 10

print(myQueue.peek())  # Output: 11
print("top" ,myQueue.top)
print("bottom" ,myQueue.bottom)
