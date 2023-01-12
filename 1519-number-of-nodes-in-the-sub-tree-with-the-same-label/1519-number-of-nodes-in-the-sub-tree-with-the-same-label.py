class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = {}
        for a,b in edges:
            if a in tree:
                tree[a].append(b)
            else:
                tree[a] = [b]
            if b in tree:
                tree[b].append(a)
            else:
                tree[b] = [a]
        res = [0]*n
        
        def dfs(node, parent):
            node_count = [0]*26
            node_count[ord(labels[node])-ord('a')] = 1
            
            for child in tree[node]:
                if child != parent:
                    child_count = dfs(child, node)
                    for i in range(26):
                        node_count[i] += child_count[i]
            res[node] = node_count[ord(labels[node])-ord('a')]
            return node_count
            
        dfs(0, None)
        return res