class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges in 'graph'.
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(src=source, dest=destination, visited=set([source])):
            if src == destination:
                return True
            for new_src in graph[src]:
                if new_src not in visited:
                    visited.add(new_src)
                    if dfs(new_src, destination, visited):  return True
            return False
        return dfs()