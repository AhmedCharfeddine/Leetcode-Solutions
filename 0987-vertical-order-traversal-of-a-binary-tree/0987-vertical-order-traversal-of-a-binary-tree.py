# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = {}
        def recurse(node, pos=(0, 0)):
            nonlocal positions
            if pos in positions:
                positions[pos] = sorted(positions[pos] + [node.val])
            else:
                positions[pos] = [node.val]
            
            if node.left:
                recurse(node.left, (pos[0]+1, pos[1]-1))
            if node.right:
                recurse(node.right, (pos[0]+1, pos[1]+1))
        
        recurse(root)
        
        # group positions by their columns
        cols = {}
        for position in positions:
            if position[1] not in cols:
                cols[position[1]] = [(positions[position], position[0])]
            else:
                cols[position[1]].append((positions[position], position[0]))
            
        res = []
        for col in sorted(cols.keys()):
            res.append([])
            for item in sorted(cols[col], key=lambda col: col[1]):
                res[-1].extend(item[0])
                
        return res