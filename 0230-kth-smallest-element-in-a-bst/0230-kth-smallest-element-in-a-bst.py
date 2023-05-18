# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_tree = []
        def recurse(node=root):
            if node:
                recurse(node.left)
                sorted_tree.append(node.val)
                recurse(node.right)
        recurse()
        return sorted_tree[k-1]