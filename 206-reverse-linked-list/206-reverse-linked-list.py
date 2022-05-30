# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        node1, node2 = head, head.next
        head.next = None
        while node2 is not None:
            temp = node2.next
            node2.next = node1
            node1 = node2
            node2 = temp
            
            
        return node1