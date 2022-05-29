#creating a sample stack

stack = []

#use .append() function to push element into stack
stack.append('a')
stack.append('b')
stack.append('c')
print("initial stack: {} ".format(stack))

#pop elements from a stack
# LIFO (last in first out) order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

#using deque for stack makes operations O(1) instead of O(n) complexity
from collections import deque

stack = deque()

#use .append() function to push element into stack
stack.append('a')
stack.append('b')
stack.append('c')
print("initial stack: {} ".format(stack))

#pop elements from a stack
# LIFO (last in first out) order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)







#implementation of Breadth First Search Algorithm

from collections import deque

graph = {
    '4' : ['8','1','5'],
    '8' : ['3','11'],
    '1' : ['7'],
    '7' : [],
    '5' : ['9','13','10'],
    '9' : ['2','6'],
    '13' : ['12'],
    '10' : ['4'],
    '3' : ['10'],
    '11' : ['2'],
    '2' : ['6'],
    '6' : [],
    '12' : []
}

visited = []
queue = deque()

"""
create a queue Q 

mark v as visited and put v into Q 

while Q is non-empty 

    remove the head u of Q 

    mark and enqueue all (unvisited) neighbors of u
"""

def bfs(visted, graph, node):
    visited.append(node)
    queue.append(node)

    print(queue)

    while queue:
       head = queue.popleft()
       print(queue)
       print(head)

       for n in graph[head]:
           if n not in visited:
               visited.append(n)
               queue.append(n)
               print(queue)
    print(visited)

    
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '4')    # function calling







