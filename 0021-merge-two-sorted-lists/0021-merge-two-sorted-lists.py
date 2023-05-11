# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        ptr1, ptr2 = list1, list2
        res = ListNode()
        node = res
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                node.val = ptr1.val
                ptr1 = ptr1.next
            else:
                node.val = ptr2.val
                ptr2 = ptr2.next
            node.next = ListNode()
            node = node.next
        
        while ptr2:
            node.val = ptr2.val
            node.next = ListNode()
            node = node.next
            ptr2 = ptr2.next
        while ptr1:
            node.val = ptr1.val
            node.next = ListNode()
            node = node.next
            ptr1 = ptr1.next
        
        node = res
        while node.next.next:
            node = node.next
        node.next = None
        return res