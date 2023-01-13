class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        if len(parent) == 1:    return 1
        n = len(parent)
        counter = Counter(parent)
        children_count = [counter[node] for node in range(n)]
        
        # queue starts with leaf nodes
        queue = deque()
        res = 1
        longest_chains = [[0, 0] for _ in range(n)]
        
        for node in range(n):
            if children_count[node] == 0:    # leaf node
                longest_chains[node][0] = 1
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            cur_parent = parent[node]
            
            # get longest chain starting from current node
            longest_chain = longest_chains[node][0]
            
            if s[node] != s[cur_parent]:
                if longest_chain > longest_chains[cur_parent][0]:
                    longest_chains[cur_parent] = [longest_chain, longest_chains[cur_parent][0]]
                elif longest_chain > longest_chains[cur_parent][1]:
                    longest_chains[cur_parent][1] = longest_chain
        
            res = max(res, longest_chains[cur_parent][0]+longest_chains[cur_parent][1] + 1)
            children_count[cur_parent] -= 1
            
            if children_count[cur_parent] == 0 and cur_parent != 0:
                longest_chains[cur_parent][0] += 1
                queue.append(cur_parent)
        
        return res