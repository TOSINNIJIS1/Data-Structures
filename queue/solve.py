quiz = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

for q in quiz:
    print(q)


# count how many stuff are in the item

def count_occurrence(values, to_find):
    number_of_occurence = 0
    for v in range(len(values)):
        if values[v] == to_find:
            number_of_occurence += 1
    return number_of_occurence

values = [1,2,2,3,3,3, 'bang', 'bang']

check_for_threes = count_occurrence(values, 'bang')
print(check_for_threes)


# Linked List store each item as an isolated Node, dynamic allocated memory
# An array is used to hold list of values but in contiguous fashion, the values are not isolated. Static allocated memory

# The first element/value in our linked list is the head
# The last element/value in our linked list is the tail
# The N represent Null or None

# 12-->39-->5-->N
# 12 is the head
# 5 is the tail
# N is the None/Null

# class Node:
#     self.value = value
#     self.next = next_node

# class LinkedList:
#     self.head = head
#     self.tail = tail

# No Node refer to the previous Node, they all refer to the next Node


# FIFO -> First In First Out

# Queue
# class Queue:
#     self.size = 0
#     self.storage = storage_data_structure


def bang(b):
    i = 1
    while i < b:
        print(i)
        i *= 2
bang(100)

