# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        hm = {}
        
        def dfs(node, path):
            if not node:    return '#'
            
            path = f"{node.val},{dfs(node.left, path)},{dfs(node.right, path)}"
            
            if path in hm:
                hm[path] += 1
                if hm[path] == 1:
                    res.append(node)
            else:
                hm[path] = 0
                
            return path
        dfs(root, '')
        return res