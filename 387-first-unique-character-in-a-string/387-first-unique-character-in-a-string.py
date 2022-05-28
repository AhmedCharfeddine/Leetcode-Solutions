class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        repeated = set()
        for i,c in enumerate(s):
            if c not in repeated:
                if c not in d:
                    d[c] = i
                else:
                    d.pop(c)
                    repeated.add(c)
        
        if len(d) == 0: return -1
        return min(d.values())