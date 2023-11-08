from cmath import inf
from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Version
def insertIntoMaxTreeRecursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or val > root.val: return TreeNode(val, root, None)

    root.right = insertIntoMaxTreeRecursive(root.right, val)

    return root

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(1)
val = 4

print(insertIntoMaxTreeRecursive(root, val))
