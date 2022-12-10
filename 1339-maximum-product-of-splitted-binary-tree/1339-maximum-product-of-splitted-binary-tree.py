# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # getting the sum of all nodes in the tree
        def get_tree_sum(node):
            if not node:    return 0
            return node.val + get_tree_sum(node.right) + get_tree_sum(node.left)
        tree_sum = get_tree_sum(root)
        
        # bottoms up iteration
        res = -math.inf
        def helper(node):
            nonlocal res
            if not node:    return 0
            cur_sum = node.val
            if node.right:  cur_sum += helper(node.right)
            if node.left:   cur_sum += helper(node.left)
            
            # compare to highest product
            cur_prod = cur_sum * (tree_sum - cur_sum)
            if cur_prod > res:
                res = cur_prod
            return cur_sum
        
        helper(root)
        return int(res % (1e9+7))