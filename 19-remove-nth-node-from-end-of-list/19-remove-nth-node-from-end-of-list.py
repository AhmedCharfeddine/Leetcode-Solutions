# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1, ptr2 = head, head
        for _ in range(n):
            ptr2 = ptr2.next
        
        # corner case: n == length
        if ptr2 is None:    
            return head.next
        
        # advance both pointers
        while ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return head