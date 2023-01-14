class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = []
        for _ in range(26): adj.append([0] * 26)
            
        for i in range(len(s1)):
            adj[ord(s1[i])-ord('a')][ord(s2[i])-ord('a')] = 1
            adj[ord(s2[i])-ord('a')][ord(s1[i])-ord('a')] = 1
        visited = set()
        
        char_map = {}
        for i in range(26):
            if i not in visited:
                # perform dfs search
                synonyms = {i}
                min_char = i
                stack = deque([i])
                while stack:
                    char = stack.pop()
                    for char2 in range(26):
                        if char2 not in synonyms and adj[char][char2] == 1:
                            synonyms.add(char2)
                            min_char = min(min_char, char2)
                            stack.append(char2)
                            visited.add(char2)
                        
                for char in synonyms:
                    char_map[chr(char + ord('a'))] = chr(min_char + ord('a'))
        
        # building the result
        res = []
        for i in range(len(baseStr)):
            res.append(char_map[baseStr[i]])
        return ''.join(res)