# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target_sum, current_sum):
            if not node:
                return False
            
            if node.left is None and node.right is None:
                if current_sum + node.val == target_sum:
                    return True
                else:
                    return False
            
            current_sum += node.val

            return dfs(node.left, target_sum, current_sum) or \
                dfs(node.right, target_sum, current_sum)
        
        return dfs(root, targetSum, 0)
        