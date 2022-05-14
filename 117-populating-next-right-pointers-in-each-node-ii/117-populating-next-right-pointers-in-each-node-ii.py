"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        d = {}
        level = 0
        self.helper(root, d, level)
        return root
    
    def helper(self, root, d, level):
        if root.left != None:
            self.helper(root.left, d, level+1)
        self.set_next(root, d, level)
        if root.right != None:
            self.helper(root.right, d, level+1)
    
    def set_next(self, root, d, level):
        if root.left != None or root.right != None:
            if root.left != None:
                if level in d:
                    d[level].next = root.left
                if root.right != None:
                    root.left.next = root.right
                    d[level] = root.right                    
                else:
                    d[level] = root.left
            else:
                if root.right != None:
                    if level in d:
                        d[level].next = root.right
                    d[level] = root.right