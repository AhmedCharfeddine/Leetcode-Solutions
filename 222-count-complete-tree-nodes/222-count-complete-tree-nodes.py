# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:    return 0
        # get depth of tree 
        depth = 0
        node = root
        while node.left: 
            node = node.left
            depth += 1
            
        def helper(node, level=0):
            if node.right:
                cont, missing_nodes = helper(node.right, level+1)
                if cont:
                    cont, missing_nodes_left = helper(node.left, level+1)
                    missing_nodes += missing_nodes_left
                return (cont, missing_nodes)
            else:
                if node.left:
                    return (False, 1)
                else:
                    if level == depth:
                        return (False, 0)
                    else:
                        return (True, 2)
        
        missing_nodes = helper(root)[1]
        return (1 << (depth+1)) - 1 - missing_nodes