# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        last_elt = -math.inf
        def helper(node):
            nonlocal res, last_elt
            
            if node.left:
                helper(node.left)
            
            res = min(res, node.val - last_elt)
            last_elt = node.val
            
            if node.right:
                helper(node.right)
                
        helper(root)
        return res