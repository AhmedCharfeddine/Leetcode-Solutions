# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        tortoise and hare algorithm
        2 cases:
        even length: hare is None
        odd length: hare is the last node
        in both cases, tortoise is the node to be deleted
        '''
        
        if not head.next:   return None
        
        # corner case: length == 2
        if not head.next.next:
            head.next = None
            return head
        
        tortoise, hare = head, head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
        tortoise.val = tortoise.next.val
        tortoise.next = tortoise.next.next
        return head