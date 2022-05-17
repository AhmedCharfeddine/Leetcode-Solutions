# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# right: True
# left: False

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        route = self.get_route(original, target, [])
        node = cloned
        while route:
            if route.pop(0):
                node = node.right
            else:
                node = node.left
        return node
        
    def get_route(self, node, target, route):
        if node == target or route == None:
            return route
        if node.right == None and node.left == None:
            return None
        if node.right:
            route_right = self.get_route(node.right, target, route + [True])
            if route_right:
                return route_right
        if node.left:
            route_left = self.get_route(node.left, target, route + [False])
            if route_left:
                return route_left
        
    