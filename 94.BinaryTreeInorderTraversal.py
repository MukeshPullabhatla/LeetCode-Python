from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    st = []
    res = []
    while root or st:
        while root:
            st.append(root)
            root = root.left
        root = st.pop()
        res.append(root.val)
        root = root.right
    return res

# Driver program to test the above functions
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))