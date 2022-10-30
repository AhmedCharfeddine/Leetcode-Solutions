# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:  return head
        dummy = ListNode(0, head)
        
        lprev, cur = dummy, head
        stop = False
        
        while True:
            # verify that there are at least k nodes remaining
            node = cur
            for _ in range(k):
                if not node:
                    stop = True            
                    break
                node = node.next
            
            # if there aren't enough nodes, stop
            if stop:
                break
            
            # reverse the k next nodes
            prev = None
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev, cur = cur, temp
            
            # correct the links
            lprev.next.next = cur
            lprev.next, lprev = prev, lprev.next
            # lprev.next    -> cur
            # lprev         -> prev
            
            #lprev = lprev.next
        return dummy.next