# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if p and not q or q and not p or p.val != q.val:  return False
        stack = deque([(p,q)])
        while stack:
            n1, n2 = stack.pop()
            if (n1.val != n2.val):    return False
            if (n1.right and n2.right):
                stack.append((n1.right, n2.right))
            elif not (not n1.right and not n2.right):
                return False
            if (n1.left and n2.left):
                stack.append((n1.left, n2.left))
            elif not (not n1.left and not n2.left):
                return False
        return True