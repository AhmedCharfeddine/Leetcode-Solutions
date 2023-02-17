# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        prev = -math.inf
        def inorder(node=root):
            nonlocal res, prev
            if not node:    return
            inorder(node.left)
            res = min(res, node.val - prev)
            prev = node.val
            inorder(node.right)
        
        inorder()
        return res