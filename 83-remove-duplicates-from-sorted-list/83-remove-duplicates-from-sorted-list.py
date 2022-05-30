# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:   return head
        ptr1, ptr2 = head, head.next
        while ptr2:
            if ptr1.val == ptr2.val:
                ptr2 = ptr2.next
                ptr1.next = ptr2
            else:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
                
        return head