# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:    return 0
        def helper(node):
            if not node:    return 0
            if node.val > high: return helper(node.left)
            elif node.val < low:    return helper(node.right)
            else:   return node.val + helper(node.right) + helper(node.left)
        return helper(root)