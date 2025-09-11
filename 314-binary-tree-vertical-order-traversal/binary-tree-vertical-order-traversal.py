# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0)])
        d = defaultdict(list)
        lo = hi = 0
        out = []

        while q:
            node, c = q.popleft()
            d[c].append(node.val)
            lo = min(lo, c)
            hi = max(hi, c)

            if node.left:
                q.append((node.left, c - 1))
            
            if node.right:
                q.append((node.right, c + 1))

        for i in range(lo, hi + 1):
            out.extend([d[i]])
        
        return out


        