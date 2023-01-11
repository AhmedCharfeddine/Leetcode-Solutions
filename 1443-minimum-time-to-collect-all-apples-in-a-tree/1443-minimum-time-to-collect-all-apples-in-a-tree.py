class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = {}
        for n1, n2 in edges:
            if n1 not in tree:
                tree[n1] = [n2]
            else:
                tree[n1].append(n2)
            if n2 not in tree:
                tree[n2] =  [n1]
            else:
                tree[n2].append(n1)
        
        visited = set()
        def dfs(node, parent=None):
            visited.add(node)
            total_time = 0
            for child in tree[node]:
                if child == parent: continue
                child_time = dfs(child, node)
                if child_time or hasApple[child]:
                    total_time += child_time + 2
            return total_time
        return dfs(0)