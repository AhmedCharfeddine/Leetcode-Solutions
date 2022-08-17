# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:    return (-1, True)
            height_right, res_right = helper(node.right)
            if not res_right:   return (0, False)
            height_left, res_left = helper(node.left)
            if not res_left:    return (0, False)
            if abs(height_left - height_right) > 1:
                return (0, False)
            return (max([height_left, height_right]) + 1, True)
        return helper(root)[1]