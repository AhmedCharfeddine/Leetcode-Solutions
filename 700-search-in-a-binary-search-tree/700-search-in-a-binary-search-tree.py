# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        search = root
        while val != search.val:
            if val > search.val:
                if search.right:
                    search = search.right
                else:
                    return None
            else:
                if search.left:
                    search = search.left
                else:
                    return None
        return search