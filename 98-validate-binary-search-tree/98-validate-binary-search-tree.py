# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:    return True
        stack = deque([[root, -math.inf, math.inf]])
        while stack:
            node, left_min, right_max = stack.pop()
            if node.right:
                if node.right.val >= right_max or node.right.val <= node.val:   return False
                stack.append([node.right, node.val, right_max])
            if node.left:
                if node.left.val <= left_min or node.left.val >= node.val:    return False
                stack.append([node.left, left_min, node.val])
        return True