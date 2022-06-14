"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:    return node
        res = node
        while node:
            if node.child:
                next_node = node.next
                sublevel_list = self.flatten(node.child)
                node.child = None
                node.next = sublevel_list
                sublevel_list.prev = node
                while node.next:
                    node = node.next
                node.next = next_node
                if next_node:
                    next_node.prev = node
            node = node.next
        return res
