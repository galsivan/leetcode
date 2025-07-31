class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node, target):
    if node is None:
        return False
    
    if node.value == target:
        return True
    
    return dfs(node.left, target) or dfs(node.right, target)