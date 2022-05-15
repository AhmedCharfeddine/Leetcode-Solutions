# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = {}
        level = 0
        self.helper(root, d, level)
        return d[max(d.keys())]
        
    def helper(self, root, d, level):
        if root.right != None:
            self.helper(root.right, d, level+1)
        if root.left != None:
            self.helper(root.left, d, level+1)
        if level in d:
            d[level] += root.val
        else:
            d[level] = root.val
        