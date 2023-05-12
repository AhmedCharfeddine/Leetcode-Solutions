# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res = ListNode()
        deq = deque()
        node = head
        while node:
            deq.append(node)
            node = node.next
        
        node = res
        pop_from_end = False
        while deq:
            if pop_from_end:
                node.next = deq.pop()
            else:
                node.next = deq.popleft()
            node = node.next
            pop_from_end = not pop_from_end
            
        node.next = None
        return res.next