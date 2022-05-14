# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        l1 = list1
        l2 = list2
        node = ListNode()
        res = node
        
        while True:
            if (l1 == None) or (l2 == None):
                if l1 == None:
                    node.val = l2.val
                    l2 = l2.next
                else:
                    node.val = l1.val
                    l1 = l1.next
            else:
                if l1.val >= l2.val:
                    node.val = l2.val
                    l2 = l2.next
                else:
                    node.val = l1.val
                    l1 = l1.next
            if (l1 == None) and (l2 == None):
                break
            node.next = ListNode()
            node = node.next
            
        return res