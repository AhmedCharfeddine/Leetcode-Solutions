# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node=root, is_left=False):
            if not node.left and not node.right and is_left:
                return node.val
            res = 0
            if node.left:
                res += helper(node.left, True)
            if node.right:
                res += helper(node.right, False)
            return res
        return helper()