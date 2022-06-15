# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)
        if not lists:   return None
        res = ListNode()
        node = res
        while lists:
            # get index of node with min val
            min_idx = lists.index(min(lists, key=lambda node:  node.val))

            # get val from min list
            node.val = lists[min_idx].val

            # and advance it
            lists[min_idx] = lists[min_idx].next

            if lists[min_idx] is None:
                lists.pop(min_idx)
                if not lists:
                    break
            
            node.next = ListNode()
            node = node.next
        return res