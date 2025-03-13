class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-order Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Pre-order Traversal
def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post-order Traversal
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

def preorder_traversal_swap(root):
    if root:
        root.left, root.right = root.right, root.left
        root.left.left, root.left.right = root.left.right, root.left.left
        root.right.left, root.right.right = root.right.right, root.right.left
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Original")
print("\nIn-order traversal")
inorder_traversal(root)

print("\nPre-order traversal")
preorder_traversal(root)

print("\nPost-order traversal")
postorder_traversal(root)
print("\n")

print("\nAfter Swap")
print("\nPre-order traversal")
preorder_traversal_swap(root)