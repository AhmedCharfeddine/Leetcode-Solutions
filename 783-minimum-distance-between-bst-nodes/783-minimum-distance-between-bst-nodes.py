# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        arr = []
        
        def inorder(node=root):            
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)
                
        inorder()
        for i in range(len(arr)-1):
            res = min(res, arr[i+1]-arr[i])
        return res