# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, cur_max, cur_min):
            arr = []
            if node.right:
                arr.extend([abs(cur_max-node.right.val), abs(cur_min-node.right.val)])
                arr.append(helper(node.right, max(node.right.val, cur_max), min(node.right.val, cur_min)))
            if node.left:
                arr.extend([abs(cur_max-node.left.val), abs(cur_min-node.left.val)])
                arr.append(helper(node.left, max(node.left.val, cur_max), min(node.left.val, cur_min)))
            if not arr: return 0
            return max(arr)
        return helper(root, root.val, root.val)