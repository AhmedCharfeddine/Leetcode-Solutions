# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return []
        res = []
        queue = deque([root])
        while queue:
            right_node = True
            for _ in range(len(queue)):
                node = queue.popleft()
                if right_node:
                    res.append(node.val)
                    right_node = False
                if node.right:  queue.append(node.right)
                if node.left:  queue.append(node.left)
        return res