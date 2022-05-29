# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        hare = head
        tortoise = head
        while hare.next is not None and hare.next.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
        return False