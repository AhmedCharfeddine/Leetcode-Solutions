# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def recurse(node, cur_sum):
            nonlocal res
            cur_sum = cur_sum * 10 + node.val
            if node.right or node.left:
                if node.right:  recurse(node.right, cur_sum)
                if node.left:  recurse(node.left, cur_sum)
            else:
                res += cur_sum
        recurse(root, 0)
        return res