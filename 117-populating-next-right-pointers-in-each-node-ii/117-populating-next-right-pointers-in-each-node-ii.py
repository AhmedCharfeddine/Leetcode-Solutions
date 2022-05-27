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
        queue = [root]
        right_node = None
        while queue:
            for _ in range(len(queue)): # traverse nodes at current level
                node = queue.pop(0)
                
                # code for set next
                if node.right != None:
                    node.right.next = right_node
                    if node.left != None:
                        node.left.next = node.right
                        right_node = node.left
                    else:
                        right_node = node.right
                elif node.left != None:
                    node.left.next = right_node
                    right_node = node.left
                
                # append queue
                if node.right != None:
                    queue.append(node.right)
                if node.left != None:
                    queue.append(node.left)
            
            right_node = None
            
        return root