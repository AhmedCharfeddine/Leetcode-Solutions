# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:    return True
        queue = deque([root])
        level = -1
        final_level = False
        level_stop = False
        while queue:
            level += 1
            if level_stop:  final_level = True
            for _ in range(len(queue)):
                node = queue.popleft()
                if (node.left or node.right) and level_stop:
                    return False
                if not node.left and node.right:
                    return False
                if not node.left or not node.right: level_stop = True
                if node.left:   queue.append(node.left)
                if node.right:  queue.append(node.right)
            if final_level and queue:
                return False
        return True