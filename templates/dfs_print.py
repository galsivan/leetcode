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

def bfs(node):
    if not node:
        return
    
    queue = [node]
    
    while queue:
        current = queue.pop(0)
        print(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


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

    print("BFS Level-Order:")
    bfs(root)