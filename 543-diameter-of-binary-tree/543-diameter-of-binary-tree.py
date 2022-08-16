# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def helper(node):
            nonlocal res
            if not node:
                return -1
            height_left = helper(node.left)
            height_right = helper(node.right)
            height = max(height_left, height_right) + 1
            diameter = height_left + height_right + 2
            if diameter > res:
                res = diameter
            return height
        
        helper(root)
        return res
        