# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:  return head
        n = 0
        node = head
        while node:
            node = node.next
            n += 1
        
        if k % n == 0:  return head
        
        stop = n - k % n - 1
        
        node = head
        i = 0
        while i < stop:
            i += 1
            node = node.next
        
        new_head = node.next
        node.next = None
        
        # find last node
        node = new_head
        while node.next:
            node = node.next
        node.next = head
        return new_head