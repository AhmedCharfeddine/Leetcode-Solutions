# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque([root])
        s = set()
        while queue:
            node = queue.pop()
            if node.val in s:
                return True
            s.add(k-node.val)
            if node.right:  queue.append(node.right)
            if node.left:   queue.append(node.left)
        return False