class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node):
    if not node:
        return
    
    dfs(node.left)
    print(node.value)
    dfs(node.right)

def dfs_inorder_reverse(node):
    if not node:
        return
    
    dfs_inorder_reverse(node.right)
    print(node.value)
    dfs_inorder_reverse(node.left)

if __name__ == "__main__":
    # Example usage
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    print("DFS In-Order:")
    dfs(root)

    print("DFS In-Order Reverse:")
    dfs_inorder_reverse(root)