class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for c1, c2 in zip(s, t):
            if c1 in d:
                d[c1] += 1
            else:
                d[c1] = 1
            if c2 in d:
                d[c2] -= 1
            else:
                d[c2] = -1
        return not any(d.values())