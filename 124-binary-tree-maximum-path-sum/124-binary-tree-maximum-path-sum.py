# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf
        def helper(node, cur_sum):
            nonlocal res
            if not node:    return
            a = node.val
            if node.right:
                right_sum = helper(node.right, cur_sum+node.val)
            else:
                right_sum = -1
            if node.left:
                left_sum = helper(node.left, cur_sum+node.val)
            else:
                left_sum = -1
                
            possible_sums = sorted([left_sum, right_sum, cur_sum], reverse=True)

            res = max(a, a+possible_sums[0], a+possible_sums[0]+possible_sums[1], res)
            return a + max(left_sum, right_sum, 0)
            
        helper(root, 0)
        return res