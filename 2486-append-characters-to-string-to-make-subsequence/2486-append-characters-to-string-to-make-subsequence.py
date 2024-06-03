class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_pos, i = 0, 0
        while t_pos < len(t) and i < len(s):
            if s[i] == t[t_pos]:
                t_pos += 1
            i += 1
        return len(t) - t_pos