# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_one(node, pv):
            if not node:    return None
            if node.val == pv:
                return node
            if node.right:
                if find_one(node.right, pv):
                    return node
            if node.left:
                if find_one(node.left, pv):
                    return node
            return None
        
        def find_two(node, pv, qv):
            if not node:    return None
            if node.val in (pv, qv):
                other = pv if node.val == qv else qv
                if find_one(node.right, other) or find_one(node.left, other):
                    return node
            if not node.right and not node.left:    return None
            if not node.right:  return find_two(node.left, pv, qv)
            if not node.left:  return find_two(node.right, pv, qv)
            rp = find_one(node.right, pv)
            lq = find_one(node.left, qv)
            if rp and lq:   return node
            rq = find_one(node.right, qv)
            lp = find_one(node.left, pv)
            if rq and lp:   return node
            if rp and rq:
                return find_two(node.right, pv, qv)
            return find_two(node.left, pv, qv)
        return find_two(root, p.val, q.val)