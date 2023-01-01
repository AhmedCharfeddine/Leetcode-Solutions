class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hm = {}
        split = s.split(' ')
        if len(split) != len(pattern):    return False
        for i in range(len(split)):
            if pattern[i] not in hm:
                hm[pattern[i]] = split[i]
            elif hm[pattern[i]] != split[i]:
                return False
        return len(set(hm.values())) == len(set(pattern))