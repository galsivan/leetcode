"""
An operating system has the following rules:

1. Each process is spawned from a parent process except the first process.
2. The parent process is aware of its children.
3. If a parent process is aborted, all the child processes get aborted.

One of the processes crashed and brought down a lot of other descendant processes (children, grandchildren, etc.) along with it. A log parser found the set of all the processes which have crashed. This collection of crashed processes, along with each crashed process's immediate children, are available to be passed to a function of your definition. Identify the ID of the process which crashed first.
"""

input = [ {'id': 15, 'children': [1,2]} , \
   {'id': 1, 'children': []} , \
   {'id': 2, 'children': []} , \
   {'id': 9, 'children': [4]} , \
   {'id': 10, 'children': [15,9]} , \
   {'id': 4, 'children': []} ]

def find_parent(processes):
    all_children = []
    
    for process in processes:
        all_children.extend(process['children'])
        
    all_children = set(all_children)
    
    for process in processes:
        if process['id'] not in all_children:
            return process['id']
        
              
print(find_parent(input))


"""
Given two arrays of integers, A and B, and a single integer value v, determine if it is possible to take exactly one element from each array (a from A, b from B), so that if we add them together, we get the given value (a + b = v).

Return true if it is possible to find a solution; false if it is not.


v = 10
A = [1,2,3]
B = [8,6,12]
result -> true (2 + 8 == 10)
"""

def is_sum(v, A, B):
    diff = set()
    
    for b in B:
        diff.add(v - b)
    
    for a in A:
        if a in diff:
            return True
    
    return False
    
print(is_sum(10, [1,2,3], [8,6,12]))



