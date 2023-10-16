from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def findMode(root) -> List[int]:
    def dfs(node, counter):
        if not node:
            return

        counter[node.val] += 1
        dfs(node.left, counter)
        dfs(node.right, counter)

    counter = defaultdict(int)
    dfs(root, counter)
    max_freq = max(counter.values())

    ans = []
    for key in counter:
        if counter[key] == max_freq:
            ans.append(key)

    return ans

# Driver program to test the above functions
root = TreeNode(7)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.right.left = TreeNode(8)
root.right.right = TreeNode(10)

print(findMode(root))