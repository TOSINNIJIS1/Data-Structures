class Node:
    def __init__(self, value = None, next_node = None):
        # the value at the linked list node
        self.value = value
        # the reference to the next node in the list.
        self.next_node = next_node


    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set the node's next_node reference to the passed in the node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # we wrap the input value into a Node
        new_node = Node(value)

        if self.head is None and self.tail is None:
            # if the list is empty, we set both the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise, if we have a non empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

        
    def add_to_head(self, value):
        new_node = Node(value) 
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def remove_tail(self):
        # return None if head is none(i.e the list is empty)
        if self.head is None and self.tail is None:
            return None
        if self.head is self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.get_value()
            current_node = self.head

            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()

            self.tail = current_node
            self.tail.set_next(None)
            return value
    


    def remove_head(self):
        # return None if there's no head and tail (i.e head and tai is empty)
        if self.head is None and self.tail is None:
            return None
        # if head has no next, then we have a single element in our list
        if self.head is self.tail:
            value = self.head.get_value()

            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def contains(self, value):
        if self.head is None and self.tail is None:
            return False
        current = self.head
        while current:
            if current.get_value() is value:
                return True
            current = current.get_next()
        return False


    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_value()

        return max_value