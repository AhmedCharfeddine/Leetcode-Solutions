# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:    return False
        slow, fast = head, head
        
        while fast:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        
        return False