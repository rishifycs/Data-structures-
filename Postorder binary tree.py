class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=' ')

# Example usage
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Post-order traversal of the binary tree:")
post_order_traversal(root)
