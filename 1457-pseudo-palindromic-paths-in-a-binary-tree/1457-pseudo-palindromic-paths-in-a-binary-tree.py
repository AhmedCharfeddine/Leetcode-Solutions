# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def backtrack(val, l):
            if val in l:    l.remove(val)
            else:   l.append(val)
        def helper(node, odds):
            nonlocal res
            # odds is a list of odd elements along the path
            if node.val not in odds:
                odds.append(node.val)
            else:
                odds.remove(node.val)
            if not node.right and not node.left:
                if len(odds) <= 1:  res += 1
            if node.right:
                helper(node.right, odds)
                backtrack(node.right.val, odds)
            if node.left:
                helper(node.left, odds)
                backtrack(node.left.val, odds)
        helper(root, [])
        return res