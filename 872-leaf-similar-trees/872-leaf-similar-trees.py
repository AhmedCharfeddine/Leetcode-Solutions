# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        value_sequence = deque([])
        
        # dfs first tree        
        stack = deque([root1])
        while stack:
            node = stack.pop()
            if node.right or node.left:
                if node.right:  stack.append(node.right)
                if node.left:   stack.append(node.left)
            else:
                value_sequence.append(node.val)

        # dfs second tree
        stack = deque([root2])
        while stack:
            node = stack.pop()
            if node.right or node.left:
                if node.right:  stack.append(node.right)
                if node.left:   stack.append(node.left)
            else:
                if not value_sequence or node.val != value_sequence.popleft():
                    return False
        
        # value_sequence should be empty by now
        return not value_sequence
