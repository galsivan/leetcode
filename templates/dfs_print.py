class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node):
    if node is None:
        return
    
    dfs(node.left)
    print(node.value)
    dfs(node.right)