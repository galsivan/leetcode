"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        q = collections.deque()
        q.append(root)
        count = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    for child in node.children:
                        q.append(child)
            count += 1
        return count
            

        