# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, s = stack.pop(-1)
            if not (node.right or node.left) and s == targetSum:
                return True
            if node.right:
                stack.append((node.right, s+node.right.val))
            if node.left:
                stack.append((node.left, s+node.left.val))
        return False