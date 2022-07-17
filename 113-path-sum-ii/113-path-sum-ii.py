# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:    return []
        res = []
        def helper(node, l, s):
            if not node.right and not node.left:
                if s+node.val == targetSum:
                    res.append(l+[node.val])
            if node.right:  helper(node.right, l+[node.val], s+node.val)
            if node.left:   helper(node.left, l+[node.val], s+node.val)
        helper(root, [], 0)
        return res