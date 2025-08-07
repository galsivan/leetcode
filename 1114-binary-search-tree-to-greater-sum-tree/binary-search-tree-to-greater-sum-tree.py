# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = [0]
        def dfs(node):
            if not node:
                return

            if not node.right and not node.left:
                node.val += prev[0]
                prev[0] = node.val
                return
            
            
            dfs(node.right)
            node.val = node.val + prev[0]
            prev[0] = node.val
            dfs(node.left)
        
        dfs(root)
        return root