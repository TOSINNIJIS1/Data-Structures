# Linked Lists: Insertion
# Append
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):    #Append
        new_node = Node(data)  # Note: if node is empty

        if self.head is None:        
            self.head = new_node 
            return


        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node 


    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print('previous node is not on the list')

            return

        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node



llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('c')

llist.prepend('eve')
llist.prepend('adam')

# a = x(5)
# print(a)