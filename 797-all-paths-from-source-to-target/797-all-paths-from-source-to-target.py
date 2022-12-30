class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def dfs(node, path):
            res = []
            if node == n-1:
                return [path]
            for neighbor in graph[node]:
                for final_path in dfs(neighbor, path + [neighbor]):
                    res.append(final_path)
            return res
        return dfs(0, [0])