# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        m, M = min(p.val, q.val), max(p.val, q.val)
        while queue:
            node = queue.popleft()
            if not (m <= node.val <= M):
                if node.right:  queue.append(node.right)
                if node.left:   queue.append(node.left)
            else:
                return node
        