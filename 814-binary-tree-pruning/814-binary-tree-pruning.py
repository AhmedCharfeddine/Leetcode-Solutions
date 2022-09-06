# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:    return None
        
        def is_prune(node):
            if not node:    return None
            right_prune = is_prune(node.right)
            left_prune = is_prune(node.left)
            if not right_prune: node.right = None
            if not left_prune:  node.left = None
            if right_prune or left_prune or node.val:
                return True
            return False
        is_prune(root)
        
        # in case of only one node with 0
        if not root.right and not root.left and not root.val:
            return None
        return root