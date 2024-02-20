class Node:
    def __init__(self, data) -> None:
        self.value = data
        self.next = None
    
class Linked_list:
    def __init__(self) -> None:
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data: int):
        # Create a new node with the given data
        newNode = Node(data)
        # If the linked list is empty, make the new node the head
        if self.head is None:
            self.head = newNode
            return
        # Otherwise, traverse to the end of the list and append the new node
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
    
    def print_list(self):
        """
        Prints the elements of the linked list.
        """
        # Start from the head node and traverse through each node, printing its value
        curNode = self.head
        while curNode:
            print(curNode.value)
            curNode = curNode.next

## Testing
linked_list = Linked_list()  # Creating an instance of Linked_list
# Appending elements to the linked list
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(8)

# Printing the elements of the linked list
linked_list.print_list()
