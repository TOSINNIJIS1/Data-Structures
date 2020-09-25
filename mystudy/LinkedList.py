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

# Binary Search
    # def iteration_depth_first_for_each(self, fn):
    #     # DFO: LIFO
    #     # Stack
    #     stack = []
    #     stack.append(self)

    #     while len(stack) > 0:
    #         current = stack.pop()

    #         if current.right:
    #             stack.append(current.right)
            
    #         if current.left:
    #             stack.append(current.left)

    #         fn(current.value)

    
    # def iteration_breadth_first_for_each(self, fn):
    #     from collections import deque

    #     # BFT: FIFO
    #     # Queue

    #     queue = deque()
    #     queue.append(self)

    #     while len(queue) > 0:
    #         current = queue.popleft()

    #         if current.left:
    #             queue.append(current.left)

    #         if current.right:
    #             queue.append(current.right)

    #         fn(current.value)