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

# Swap
def swap_subtrees(root):
    if root:
        root.left, root.right = root.right, root.left
        swap_subtrees(root.left)
        swap_subtrees(root.right)


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

print("Swapping")
swap_subtrees(root)

print("Inorder Traversal After Swap:")
inorder_traversal(root)

print("\nPreorder Traversal After Swap:")
preorder_traversal(root)

print("\nPost Order Traversal After Swap:")
postorder_traversal(root)

