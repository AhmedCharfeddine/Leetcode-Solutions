class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        hm = {}
        for pair in dislikes:
            if pair[0] in hm:
                hm[pair[0]].add(pair[1])
            else:
                hm[pair[0]] = {pair[1]}
            if pair[1] in hm:
                hm[pair[1]].add(pair[0])
            else:
                hm[pair[1]] = {pair[0]}
        
        colors = [-1] * (n+1)   # will contain 0 for group1 and 1 for group2
                                # 1-indexed for consistency with the problem labels
        for i in range(1, n):
            if colors[i] == -1 and i in hm:
                # start a BFS search
                colors[i] = 0   # arbitrary
                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    for neighbor in hm[node]:
                        if colors[node] == colors[neighbor]:
                            return False
                        if colors[neighbor] == -1:
                            colors[neighbor] = 1 - colors[node]
                            queue.append(neighbor)
        return True