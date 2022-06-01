# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return None
        def helper(root, l):
            l.append(root.val)
            if root.left:
                helper(root.left, l)
            if root.right:
                helper(root.right, l)
        l = []
        helper(root, l)
        return l