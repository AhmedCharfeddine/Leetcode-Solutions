# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:    return 0
        res = 0
        def helper(node, l, s):
            nonlocal res
            l.append(node.val)
            s += node.val

            # look through specific sublists
            s1 = s
            for i in range(len(l)):
                if s1 == targetSum:
                    res += 1
                s1 -= l[i]
            
            if node.right:
                helper(node.right, l, s)
                l.pop(-1)
            if node.left:
                helper(node.left, l, s)
                l.pop(-1)
        helper(root, [], 0)
        return res