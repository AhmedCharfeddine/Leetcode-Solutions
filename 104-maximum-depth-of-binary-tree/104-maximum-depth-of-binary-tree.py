# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        if not root:    return 0
        def helper(root, level):
            if root.right:
                rd = helper(root.right, level+1)
            else:
                rd = -math.inf
            if root.left:
                ld = helper(root.left, level+1)
            else:
                ld = -math.inf
                
            return max(level, ld, rd)
        
        return helper(root, 1)