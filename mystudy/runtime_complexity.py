# Runtime Complexity
# An objective way to measure the efficiency of code/algorithms

# Constant Time: An operation that take the same amount of time regardless of the input size
    # List Indexing
    # fetching from dictionary via key
    # O(1)

command = [1,2,3,4,5,6]
print(command[1]) # doesn't depend on the size of element/value
Bang = 'yo'
command = { 1: Bang }
print(command[1])

# Linear Time: An operation that depend on the size of the input(element/value); 
# the time the operation takes increases linearly with the input size
    # For loops
    # Toss out constant value with Big O
    # O(n)

command = [1,2,3,4,5,6]
dictionary = {
    'command': {
        'number': 123456
    }    
}
for commands in command:
    print(commands)
 
print(dictionary)

for key, value in dictionary.items():
    print(key, value)

# Quadratic Time: An operation that depend on the size of the input(element/value); 
# the time the operation takes increases quadratically with the input size
    # Enumerating all possible pairs from two lists:
        # length of list 1 * length of list 2
        # O(m*n) or O(n^2)

commands = [1,2,3,4,5,6]

for x in commands:
    for y in commands:
        print(x, y)

# O(1) < O(n) < O(n * m) or O(n^2)