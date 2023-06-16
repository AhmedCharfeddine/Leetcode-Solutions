# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = {}
        
        def recurse(node, coordinates=(0,0)):
            nonlocal hm
            if node:
                if coordinates not in hm:
                    hm[coordinates] = [node.val]
                else:
                    hm[coordinates].append(node.val)
                
                row,col = coordinates
                recurse(node.left, (row+1,col-1))
                recurse(node.right, (row+1, col+1))
            
        
        recurse(root)
        
        cols = {}
        for coordinates, values in hm.items():
            row, col = coordinates
            if col in cols:
                cols[col].append((values, row))
            else:
                cols[col] = [(values, row)]
        
        res = []
        for col in sorted(cols.keys()):
            col_value = cols[col]
            col_value.sort(key=lambda item: item[1])
            new_row = []
            for item in col_value:
                new_row.extend(sorted(item[0]))
            res.append(new_row)
            
        return res
