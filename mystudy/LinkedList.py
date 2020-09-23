class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)


# We need to start from the head to the tail 
# Head => We had to start from the head and traverse all the way to the end of the linked list to add a new element
# Tail