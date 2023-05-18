class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(map(len, strs))
        prefix_len = 0
        for i in range(min_len):
            if len({s[i] for s in strs}) != 1:
                return strs[0][:i]
        return strs[0][:min_len]