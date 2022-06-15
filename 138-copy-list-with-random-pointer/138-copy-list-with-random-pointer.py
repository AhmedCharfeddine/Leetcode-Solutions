"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:    return None
        hm = {head: Node(head.val)}
        cur = head
        while cur:
            clone = hm[cur]
            
            if cur.next and cur.next not in hm:
                hm[cur.next] = Node(cur.next.val)
            
            if cur.random and cur.random not in hm:
                hm[cur.random] = Node(cur.random.val)
            
            if cur.next:
                clone.next = hm[cur.next]
            if cur.random:
                clone.random = hm[cur.random]
            
            cur = cur.next
        return hm[head]