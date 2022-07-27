# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:    return root
        node = root
        while node.right:
            if node.left:
                right = node.right
                node.right = self.flatten(node.left)
                node.left = None
                while node.right:
                    node = node.right
                node.right = right
            else:
                node = node.right
                
        # deal with the case where there's no right node but a there's a left node
        if node.left:
            node.right = self.flatten(node.left)
            node.left = None
        return root