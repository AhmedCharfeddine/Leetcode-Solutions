# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None and head.val == val:
            return None
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return head
        node = head
        while node is not None and node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head