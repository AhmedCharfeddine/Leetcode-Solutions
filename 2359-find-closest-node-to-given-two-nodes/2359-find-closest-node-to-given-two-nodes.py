class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, dictionary, dist=0):
            if edges[node] == -1 or edges[node] in dictionary:
                return dictionary
            dictionary[edges[node]] = dist+1
            return dfs(edges[node], dictionary, dist+1)
        res = -1
        path_len = math.inf
        path1 = dfs(node1, {node1:0})
        path2 = dfs(node2, {node2:0})
        for i in range(len(edges)):
            if i in path1 and i in path2:
                if path_len > max(path1[i], path2[i]):
                    path_len = max(path1[i], path2[i])
                    res = i
                elif path_len == max(path1[i], path2[i]):
                    res = min(res, i)
        return res