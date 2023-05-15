# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []
        res = []
        def recurse(level=[root], zigzag=True):
            if not level:   return
            nonlocal res
            cur_level = []
            next_level = []
            if zigzag:
                level_iterator = level[::-1]
            else:
                level_iterator = level
            for node in level_iterator:
                cur_level.append(node.val)
            for node in level:
                if node.right:  next_level.append(node.right)
                if node.left:   next_level.append(node.left)
            res.append(cur_level)
            recurse(next_level, not zigzag)
        recurse()
        return res