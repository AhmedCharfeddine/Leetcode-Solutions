# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:   return head
        ptr1 = head
        while ptr1.next:
            if ptr1.next.val == ptr1.val:
                ptr1.next = ptr1.next.next
            else:
                ptr1 = ptr1.next
                
        return head