# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        node = res
        overflow = 0
        while l1 and l2:
            s = l1.val + l2.val + overflow
            overflow = 0
            if s >= 10:
                overflow += 1
                s %= 10
            node.val = s
            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                node.next = ListNode()
                node = node.next
        if l1:
            l = l1
        else:
            l = l2
        while l:
            s = l.val + overflow
            overflow = 0
            if s >= 10:
                overflow = 1
                s %= 10
            node.val = s
            l = l.next
            if l:
                node.next = ListNode()
                node = node.next
        if overflow:
            node.next = ListNode(1)
        return res